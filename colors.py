#######################################
#                                     #
#   Файл для работы проекта:          #
#   Чат-бот                           #
#                                     #
#   Создан учеником:                  #
#   Владислав Косинский Станиславович #
#######################################
def red(txt): # начинаю создавать функции цветов
    print("\033[31m{}\033[0m" .format(txt))
def boldred(txt):
    print("\033[31m\033[1m{}\033[0m" .format(txt))
def boldgreen(txt):
    print("\033[32m\033[1m{}\033[0m" .format(txt))
def green(txt):
    print("\033[32m{}\033[0m" .format(txt))
def blue(txt):
    print("\033[34m{}\033[0m" .format(txt))
def boldblue(txt):
    print("\033[34m\033[1m{}\033[0m" .format(txt))
class colour: # Создаю класс colour для работы будущем в файле main.py
    CRED = '\033[31m'
    CBOLDRED = '\033[31m\033[1m'
    CBOLDGREEN = '\033[32m\033[1m'
    CGREEN = '\033[32m'
    CBLUE = '\033[34m'
    CBOLDBLUE = '\033[34m\033[1m'
    END = '\033[0m'
