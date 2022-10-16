
import vosk
import sys
import sounddevice as sd
import queue
import json
import speech_recognition


model = vosk.Model("model_small")

samplerate = 16000
device = 1

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
            # else:
            #    print(rec.PartialResult())



# recognizer = speech_recognition.Recognizer()
# microphone = speech_recognition.Microphone()
#
#
# def record_and_recognize_audio():
#     """
#     ?????? ? ????????????? ?????
#     """
#
#     # voice_recognizer = sr.Recognizer()
#     # voice_recognizer.dynamic_energy_threshold = False
#     # voice_recognizer.energy_threshold = 1000
#     # voice_recognizer.pause_threshold = 0.5
#
#     with microphone:
#         recognized_data = ""
#
#         # ????????????? ?????? ??????????? ????
#         recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
#
#         try:
#             audio = recognizer.listen(microphone, timeout=None, phrase_time_limit=4)
#
#         except speech_recognition.WaitTimeoutError:
#             print("Can you check if your microphone is on, please?")
#             return
#         try:
#             recognized_data = recognizer.recognize_google(audio, language="ru").lower()
#         except speech_recognition.UnknownValueError:
#             pass
#
#         return recognized_data


