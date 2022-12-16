from db_bot import *
from colors import *
import time
import random
import statics

def base_ask(ask):
    if ask in start:
        print(random.choice(privet))
    while True:
        ask = input().lower()
        hello = 1
        if "stop" in ask:
            while True:
                global user_text
                user_text = "stop"
                if user_text == "stop":
                    break
                else:
                    user_text = "stop"
            break
        if "поиграем в рулетку" in ask:
            start_roulet(ask)
            break
        elif ask in start:
            hello+=1

            if hello < 5:
                print(random.choice(privet))
            else:
                print(random.choice(much_hello))
            if hello < 5:
                print("Ну привет. У тебя очень плохая карма!")
            else:
                print(random.choice(much_hello))
        elif "посоветуй игру" in ask:
            print(1)
            break
        elif ask in ask_talkings:
            talking(ask)
            break
def talking(ask):
    while True:
        print("Давайте! Как у вас дела?") # спрашиваем у пользователя как дела
        ask = input("").lower()            # получаем от пользователя ответ
        if "stop" in ask:
            while True:
                global user_text
                user_text = "stop"
                break
        if "нормально" in ask  or  "хорошо" in ask: # Если пользователь вводит нормально или хорошо
            print(random.choice(okay)) # Выбираем рандомное слово из переменной okay
        
        elif "stop" in ask: # При вводе stop прекращаем этот цикл
            green("Прекрашаем разговор..."+colour.CBLUE+" :(") # Выводим такой печальный текст
            break # Разрываем этот цикл
        
        elif "плохо" in ask  or  "ужасно" in ask: # Если пользователь вводит плохо или ужасно то
            print("Желаю удачи тебе") # пишет вот такой текст поддержки
        
        else: # Если ничего не совпадает то
            print("Понятно, удачи тебе") # Пишем текст которые будет совпадать в многих случаях
       
        while True: #начинаем цикл после вопроса для пользователя как у него дела
            ok_no = ["okay","nope"] # Создаём переменную ok_no для того, чтобы потом с пользователем общаться
            resultok_no = random.choice(ok_no) # Потом выбираем рандомное слово из этого списка
            ask = input("").lower() # просим пользователя вести что ни будь
            
            if "поговорим о другом" in ask: # Если пишет пользователь такое, то разрываем цикл с согласием
                print("Давай!")
                break
            elif "stop" in ask: # При вводе stop прекращаем этот цикл
                green("Прекрашаем разговор..."+colour.CBLUE+" :(") # Выводим такой печальный текст
                break # Разрываем этот цикл
            elif "как дела" in ask or "как дела?" in ask: # При вопросе как у чат-бота дела то мы отвечаем
                print(random.choice(dela)) # рандомное слово из переменной dela в файле peremenya.py
            
            elif "что делаешь?" in ask or "что делаешь" in ask: # При таком вопросе бот отвечает
                print("Общаюсь с тобой, а ты?") # вот этот текс и спрашивает у пользователя тоже
                ask = input().lower() # потом делаем "пустышку"
                print(random.choice(okay)) # После этого бот пишет рандомное слово 
            
            elif "кто ты" in ask or "кто ты?" in ask or "что ты" in ask or "что ты?" in ask: # При таком вопросе бот ответчает
                print(random.choice(whoyou)) # любое слово из переменной whoyou
            
            elif "желаю удачи" in ask: # Желаем пользователю тоже удачи
                print("И тебе всего удачи!")
            
            elif "понятно" in ask: # При понятно отвечаем пользователю 'Понятно-понятно)'
                print("Понятно-понятно)")
            
            elif "спроси у меня" in ask or "спросишь у меня" in ask or "спроси у меня?" in ask or "спросишь у меня?" in ask: # При таком вопросе делаем следующее
                print("Хорошо, давай я у тебя спрошу:") #Спрашиваем
                a = random.choice(vopros) # Берём любое слово из переменной vopros
                print(a) # Пишем этот вопрос
                ask = input().lower() # Спрашиваем у пользователя ответ
                
                if "делаешь?" in a: # Если "делаешь?" в пременной a где у нас вопрос то выполняем такие действия
                    if "ничего" in ask: # При ничего то тогда пишем это
                        print("Тогда что-нибудь да и поделай! Пожалуйста)")
                    else:# Иначе пишем любое согласие
                        print(random.choice(okay))
                
                elif "кушал?" in a: # Если "кушал?" в пременной a где у нас вопрос то выполняем такие действия
                    if "ничего" in ask: # При ничего то тогда пишем это
                        print("Тогда что-нибудь да и поешь! Пожалуйста)")
                    else:# Иначе пишем любое согласие
                        print(random.choice(okay))
                
                elif "stop" in ask: # При Stop разрываем цикл
                    break 
            
            elif "умер" in ask or "умерла" in ask or "умрёт" in ask: # Если пользователь введёт что-то такое, то мы пишем слова поддержки
                print("Сочувствую, надеюсь всё наладиться!") 
            
            elif ask !=  dela and vopros: # Если ответ пользователя не равно перменным dela и vopros то пишем такое
                if resultok_no == "okay": # проверяем, если в переменной resultok_no равен тексту okay То пишем такое
                    print(random.choice(okay))
                else: # иначе
                    print(random.choice(nope))
           
            elif ask != vopros: # если нет в vopros то пишем ничего
                print("Ничто")
            
            elif ask != dela: # а если при dela то пишем понятно, желаю удачи
                print("Понятно, желаю удачи") 

            else: # Если ничего из этого не случилось то пишем такое (почти никогда не используется после обновления кода)
                print("Извини, не понял тебя, давай я у тебя спрошу:")
                a = random.choice(vopros)
                print(a)
                ask = input().lower()
                if "делаешь?" in a:
                    if "ничего" in ask:
                        print("Тогда что-нибудь да и поделай! Пожалуйста)")
                    else:
                        print(random.choice(okay))
                
                elif "кушал?" in a:
                    if "ничего" in ask:
                        print("Тогда что-нибудь да и поешь! Пожалуйста)")
                    else:
                        print(random.choice(okay))
                
                elif "stop" in ask:
                    break  # Конец что я добавил

def start_roulet(ask):
    global user_text
    user_text = ""
    print("Давайте! Играем до последней крови...\nПистолет достаётся мне первым\n") # Потом отвечает такое бот
    pstl = ["0","0","1","0","0","0","0","0"] # Создаём имитацию одного барабана револьера
    random.shuffle(pstl) # Перемешиваем данные
    while True: # создаём цикл
        boldred("кручу барабан...")
        time.sleep(1) # Программа ожидает пока пройдёт 1 секунда
        shtrslt = random.choice(pstl) # выбираем в переменную любое число
        random.shuffle(pstl) # опять перемешиваем данные в pstl
        boldgreen("Подношу к голове револьер...")
        time.sleep(1.3) # Программа ожидает пока пройдёт 1.4 секунды
    
        if shtrslt == "1": # если выпало 1 то проиграл
            boldred("ВЫСТРЕЛ!")
            time.sleep(0.3)
            red("О нет! Я погиб.. Удача твоя, выхожу из игры")
            break # разрываем в последствии цикл
                
        else: # если нет, то продолжаем цикл
            boldred("ЩЕЛЧЁК!")
            time.sleep(0.3) # Программа ожидает пока пройдёт 0.3 секунды
            green("Я живой, даю тебе пистолет...")
            
            boldblue("Крути барабан, или отказываешься? Да или нет") # Спрашиваем пользователя продолжать игру?
            ask = input().lower() 
            
        if "да" in ask: # Если да то разрываем цикл с спокойной душой
            green("Ну тогда давай, удачи")
            break
            
        elif "нет" in ask: # Если нет, то желаем удачи...
            green("Тогда хорошо, желаю удачи, кручу барабан..")
            time.sleep(1.3)
            shtrslt = random.choice(pstl)
            random.shuffle(pstl)
                
            if shtrslt == "1": # выполняем точно так же пока не попадётся 1 у кого либо или пользователь откажеться играть
                boldred("ВЫСТРЕЛ!")
                time.sleep(0.3)
                red("Ты мертв, тебе не повезло..")
                green("Выходим из игры")
                break
            else:
                boldred("ЩЕЛЧЁК!")
                time.sleep(0.3)
                boldgreen("Ты живой! Продолжаем? Да или нет?")
                ask = input().lower()

                if "да" in ask:
                    green("Хорошо, пожелай мне удачи\n")
                else:
                    green(random.choice(okay))
                    break
                     