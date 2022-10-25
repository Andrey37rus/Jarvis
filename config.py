from turn_off_restart_sleep import shutdown, sleep_mode, restart
from gree import home, good_days, thanks, i_need
from minimize_maximize_window import show_window, show_minimize
from open_close_program import run_programs, close_program
from show_list_programms import list_programs
from clear_list_programms import clear
from adding_programms import add_program
from counter_strike_go import counter_strike
from reproduction import up, down, soundless, sound
from open_links import open, search_by_internet, text_search


VA_NAME = 'Джарвис'

VA_VER = "2.0"

VA_ALIAS = ('джарвис', 'дарвис', 'харвиc', 'жарвис', 'джой', 'джервис', 'чарльз', 'чавез', 'чавес', 'jarvis', 'джаред',
            'джери', 'чарли', 'джек', 'джеки', 'джейк')


chunk = {
    'доброе': ('доброе', 'доброго', 'доброва', 'добрым', 'доброй'),
    'утро': ('утро', 'утречко', 'утречка', 'утра', 'утром'),
    'я': ('я', 'мы'),
    'открыть': ('открыть', 'открой', 'открывай', 'открываю', ''),
    'дома': ('дома', 'домо', 'домыв', 'домой'),
    'запустить': ('запусти', 'запускай', 'запустить'),
    'добавить': ('добавить', 'добавь'),
    'программа': ('программу', 'программа', 'программы', 'программ'),
    'выключить': ('выключить', 'выключать', 'выключи'),
    'компьютер': ('компьютер', 'комп', 'блок', 'комб', 'систему'),
    'чистый': ('чистый', 'чистой', 'чистая', 'чистое', 'очистить'),
    'лист': ('лист', 'лес', 'лис', 'пист'),
    'протокол': ('протокол', 'чистокол', 'мотокол'),
    'список': ('список', 'списки', 'списка'),
    'перезагрузить': ('перезагрузить', 'перезагрузка', 'перенагрузка'),
    'спящий': ('спящий', 'спящой'),
    'режим': ('режим', 'режим'),
    'закрыть': ('закрыть', 'закрыто', 'закрой', 'закрыл', 'закрыла', 'закрою'),
    'свернуть': ('свернуть', 'свернул', 'свёрнутый', 'сверни', 'свернулось', ''),
    'развернуть': ('развернуть', 'развернул', 'разворачивай', 'развернутый', 'разверни'),
    'купить': ('купить', 'купи', 'закупи', 'покупай'),
    'play': ('play', 'плэй', 'стоп', 'stop'),
    'громче': ('громче', 'громко', 'погромче'),
    'тихо': ('тихо', 'тише', 'потише'),
    'следующий': ('следующий', 'следую', 'следовать', 'следущий'),
    'трек': ('трек', 'трэк', 'трак', 'трект'),
    'предыдущий': ('предыдущий', 'преудущий', '', ''),
    'спасибо': ('спасибо', 'спасиба', 'благодарю', 'блогодаря', 'спасибки', 'спасибочки'),
    'ты': ('ты', 'тот', 'та', 'то'),
    'здесь': ('здесь', 'здеся', 'сдесь'),
    'звук': ('звук', 'звуки', 'звонк', 'звонкий', 'звонок', 'звука'),
    'без': ('без', 'бес', ''),
    'искать': ('искать', 'ищу', 'ищи', 'найди', 'найти'),
    'поиск': ('поиск', 'поискать', '')
    }


commands = {
    'ты здесь': i_need,
    'спасибо': thanks,
    'громче': up,
    'тихо': down,
    'без звук': soundless,
    'звук': sound,
    # 'следующий трек': next_trak,
    # 'предыдущий трек': previous_track,
    'открыть': open,
    'запустить': run_programs,
    'добавить программа': add_program,
    'выключить компьютер': shutdown,
    'доброе утро': good_days,
    'протокол чистый лист': clear,
    'перезагрузить компьютер': restart,
    'спящий режим': sleep_mode,
    'закрыть': close_program,
    'выключить': close_program,
    'список программа': list_programs,
    'свернуть': show_minimize,
    'развернуть': show_window,
    'я дома': home,
    # 'play': play_music,
    ('купить', 'купи', 'возьми', 'взять', 'позови', 'позвать'): counter_strike,
    'искать': search_by_internet,
    'поиск': text_search,

}











