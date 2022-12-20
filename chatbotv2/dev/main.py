from db_bot import *
import doing
import random
print("""
Список что может бот:

Поиграем в рулетку
Посоветуй игру
Поболтаем?
Загадку
""")
user_text = input().lower()
doing.base_ask(user_text)
while True:
    user_text = input().lower()
    if "stop" in user_text:
        break
    if "поиграем в рулетку" in user_text:
        doing.start_roulet(user_text)
    elif user_text in start:
        doing.base_ask(user_text)
    elif "посоветуй игру" in user_text:
        print(1)
    elif user_text in ask_talkings:
        doing.talking(user_text)
    else:
        print(random.choice(huh))