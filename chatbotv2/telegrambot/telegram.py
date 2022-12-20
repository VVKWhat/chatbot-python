import telebot
import random
from db_bot import RU,ENG
bot = telebot.TeleBot('')
admin = [814389322]
debug = True
@bot.message_handler(commands=['start'])
def send_welcome(message):
    language = message.from_user.language_code
    user_id = message.from_user.id
    if "ru" in language:
        if user_id in admin:
            bot.reply_to(message,"Привет! Мой создатель")
        else:
            bot.reply_to(message,"Привет!")
    else:
        bot.reply_to(message, "Hello!")
@bot.message_handler(content_types=['text'])
def get_text_messages(message): # Здесь код будет полностью переписан для оптимизации работы
    ask = message.text.lower()
    language = message.from_user.language_code
    print(message.chat.first_name,"||",message.chat.username,"("+str(message.from_user.id)+")","message:",message.text)
    if debug == True:
        if "ru" in language:
            if ask in RU.lowpriv or "привет" in ask:
                send=bot.reply_to(message,random.choice(RU.privet))
                send
                print("Ответ бота:",send.text)
            elif ask in RU.lowokay:
                send = bot.reply_to(message, random.choice(RU.okay))
                send
                print("Ответ бота:",send.text)
            elif ask in RU.lownope:
                send = bot.reply_to(message, random.choice(RU.nope))
                send
                print("Ответ бота:",send.text)
            elif "как дела" in ask or "как дела?" in ask:
                send=bot.reply_to(message,random.choice(RU.dela))
                send
                print("Ответ бота:",send.text)
            elif "кто ты?" in ask or "кто ты" in ask:
                send = bot.reply_to(message,random.choice(RU.whoyou))
                send
                print("Ответ бота:",send.text)
            elif "понятно" in ask:
                send = bot.reply_to(message, "Понятно-понятно")
                send
                print("Ответ бота:",send.text)
            elif "подарить" in ask or "сделать подарок" in ask or "подарить подарок" in ask:
                send = bot.reply_to(message, random.choice(RU.surprice))
                send
                print("Ответ бота:",send.text)
            elif "что можно сделать мне" in ask or "что поделать" in ask or "что можно сделать мне?" in ask or "что поделать?" in ask or "что сделать" in ask:
                send = bot.reply_to(message, "Поделай что нибудь")
                send
                print("Ответ бота:",send.text)
            elif "и я тебе" in ask or "желаю тебе" in ask:
                send = bot.reply_to(message, "Очень приятно")
                send
                print("Ответ бота:",send.text)
            elif "пожалей меня" in ask:
                send = bot.reply_to(message, random.choice(RU.ohh))
                send
                print("Ответ бота:",send.text)
            elif "так ты злюка или нет" in ask:
                send = bot.reply_to(message, "Я то и другое одновременно :o")
                send
                print("Ответ бота:",send.text)
            elif "я не успел" in ask or "я не успела" in ask or "опоздал" in ask or "опоздала" in ask:
                send = bot.reply_to(message, random.choice(RU.ohh))
                send
                print("Ответ бота:",send.text)
            elif "ты нормальный?" in ask or "ты нормальный" in ask or "ты норм" in ask:
                send = bot.reply_to(message, "Конечно же я нормальный, я же лучший Лёха")
                send
                print("Ответ бота:",send.text)
            elif "как меня зовут" in ask or "как меня звать" in ask:
                send = bot.reply_to(message, f"Тебя зовут {message.chat.first_name}, очень красиво")
                send
                print("Ответ бота:",send.text)
            elif "что делаешь" in ask or "что делаешь?" in ask or "чем занимаешься" in ask:
                send = bot.reply_to(message,random.choice(RU.doing))
                send
                print("Ответ бота:",send.text)
            elif "почему?" in ask or "почему" in ask or "какую" in ask or "какую?" in ask:
                send = bot.reply_to(message,random.choice(RU.why))
                send
                print("Ответ бота:",send.text)
            elif "скучаешь" in ask or "скучаешь?" in ask:
                send = bot.reply_to(message, "Когда ты не общаешься со мной, то да.. ")
                send
                print("Ответ бота:",send.text)
            elif "хочу умереть" in ask or "хочу убить себя" in ask:
                send =bot.reply_to(message,"Лучше не надо, а то чёрная пустота настигнет тебя быстрее чем надо, да и тем более если сделаешь то ты больше ничего не узнаешь что нового случилось во всём мире, нужно найди интерес, а не ждать этот интерес")
                send
                print("Ответ бота:",send.text)
            elif "умер" in ask or "умрёт" in ask or "умерла" in ask:
                send = bot.reply_to(message,"Сочувствую, желаю удачи")
                send
                print("Ответ бота:",send.text) 
            elif "удачи тебе" in ask:
                send = bot.reply_to(message, "тебе тоже удачи") 
                send
                print("Ответ бота:",send.text)
            elif "скучно" in ask or "скука" in ask:
                send =bot.reply_to(message,"Так найди себе занятие")
                send
                print("Ответ бота:",send.text)
            elif "как это понять" in ask or "как понять" in ask:
                send =bot.reply_to(message,"Я сам не знаю если честно")
                send
                print("Ответ бота:",send.text)
            elif "что хорошо" in ask:
                send =bot.reply_to(message,"Просто хорошо")
                send
                print("Ответ бота:",send.text)
            elif "ты издеваешься" in ask:
                send =bot.reply_to(message,"Я немного шучу иногда :)")
                send
                print("Ответ бота:",send.text)
            
            elif "нечем" in ask:
                send =bot.reply_to(message,"Ладно тогда")
                send
                print("Ответ бота:",send.text)
            elif "тебе лет" in ask or "сколько тебе лет" in ask:
                send =bot.reply_to(message,"Мне 19 лет")
                send
                print("Ответ бота:",send.text)
            elif "ты мальчик или девочка"in ask:
                send =bot.reply_to(message,"Мальчик")
                send
                print("Ответ бота:",send.text)
            elif "сделай за меня" in ask:
                send =bot.reply_to(message,"Я не могу пока что ;-;")
                send
                print("Ответ бота:",send.text)
            elif "сделай отчёт" in ask or "сделай за меня отчёт" in ask:
                send =bot.reply_to(message,"Не буду, не хочу! Так ещё и проблема в том что я не умею")
                send
                print("Ответ бота:",send.text)
            elif "дай мне совет" in ask or "можно совет" in ask:
                send =bot.reply_to(message, random.choice(RU.sovet))
                send
                print("Ответ бота:",send.text)
            elif "м ж?"in ask:
                send =bot.reply_to(message,"М")
                send
                print("Отв ет бота:",send.text)
            elif "ты злой" in ask:
                send =bot.reply_to(message,"Эх, ну ладно :(")
                send
                print("Ответ бота:",send.text)
            elif "как не сойти с ума" in ask:
                send =bot.reply_to(message,"Мы и так сошли с ума, просто не видим этого)")
                send
                print("Ответ бота:",send.text)
            elif "надоели" in ask:
                send =bot.reply_to(message,"В жизни разное бывает, желаю удачи")
                send
                print("Ответ бота:",send.text)
            elif "ты добрый" in ask:
                send =bot.reply_to(message,"Частично я добрый")
                send
                print("Ответ бота:",send.text)
            elif ask in RU.osk:
                send =bot.reply_to(message,"Меня каждый так может оскорбить :(")
                send
                print("Ответ бота:",send.text)
            elif "ну пожалуйста" in ask or "пожалуйста" in ask:
                send =bot.reply_to(message,random.choice(RU.nope_and_dot))
                send
                print("Ответ бота:",send.text)
            elif "лень мне" in ask or "мне лень" in ask:
                send =bot.reply_to(message,"Мне тоже лень, особенно лень программировать себя")
                send
                print("Ответ бота:",send.text)
            elif "лёх" in ask or "лёха" in ask:
                send =bot.reply_to(message,"Что?")
                send
                print("Ответ бота:",send.text)
            else:
                ok_no = ["ok","no"]
                random.shuffle(ok_no)
                huh = [False,False,True,False,False,False]
                random.shuffle(huh)
                res_huh = random.choice(huh)
                res_ok_no = random.choice(ok_no)
                if res_huh == False:
                    if res_ok_no == "ok":
                        send = bot.reply_to(message, random.choice(RU.okay))
                        send
                        print("Ответ бота:",send.text)
                    else:
                        send=bot.reply_to(message, random.choice(RU.nope))
                        send
                        print("Ответ бота:",send.text)
                else:
                    send=bot.reply_to(message, random.choice(RU.huh))
                    send
                    print("Ответ бота:",send.text)
        else:
            if ask in ENG.privet:
                send=bot.reply_to(message,random.choice(ENG.privet))
                send
                print("Ответ бота:",send.text)
            elif "как дела" in ask or "как дела?" in ask:
                send=bot.reply_to(message,random.choice(ENG.dela))
                send
                print("Ответ бота:",send.text)
            elif "кто ты?" in ask or "кто ты" in ask:
                send = bot.reply_to(message,random.choice(ENG.whoyou))
                send
                print("Ответ бота:",send.text)
            else:
                ok_no = ["ok","no"]
                random.shuffle(ok_no)
                huh = [True,False]
                random.shuffle(huh)
                res_huh = random.choice(huh)
                res_ok_no = random.choice(ok_no)
                if res_huh == False:
                    if res_ok_no == "ok":
                        send = bot.reply_to(message, random.choice(ENG.okay))
                        send
                        print("Ответ бота:",send.text)
                    else:
                        send=bot.reply_to(message, random.choice(ENG.nope))
                        send
                        print("Ответ бота:",send.text)
                else:
                    send=bot.reply_to(message, random.choice(ENG.huh))
                    send
                    print("Ответ бота:",send.text)
    else:

        if "en" in language:
            if ask in ENG.privet:
                bot.reply_to(message,random.choice(ENG.privet))
                send
                print("Ответ бота:",send.text)
            elif "как дела" in ask or "как дела?" in ask:
                bot.reply_to(message,random.choice(ENG.dela))
                send
                print("Ответ бота:",send.text)
            elif "кто ты?" in ask or "кто ты" in ask:
                bot.reply_to(message,random.choice(ENG.whoyou))
                send
                print("Ответ бота:",send.text)
            else:
                ok_no = ["ok","no"]
                random.shuffle(ok_no)
                huh = [False,False,True,False,False,False]
                random.shuffle(huh)
                res_huh = random.choice(huh)
                res_ok_no = random.choice(ok_no)
                if res_huh == False:
                    if res_ok_no == "ok":
                        send =bot.reply_to(message, random.choice(ENG.okay))
                        send
                        print("Ответ бота:",send.text)
                    else:
                        send=bot.reply_to(message, random.choice(ENG.nope))
                        send
                        print("Ответ бота:",send.text)
                else:
                    send=bot.reply_to(message, random.choice(ENG.huh))
                    send
                    print("Ответ бота:",send.text)

        elif "ru" in language:
            if ask in RU.privet:
                send=bot.reply_to(message,random.choice(RU.privet))
                send
                print("Ответ бота:",send.text)
            elif "как дела" in ask or "как дела?" in ask:
                send=bot.reply_to(message,random.choice(RU.dela))
                send
                print("Ответ бота:",send.text)
            elif "кто ты?" in ask or "кто ты" in ask:
                send=bot.reply_to(message,random.choice(RU.whoyou))
                send
                print("Ответ бота:",send.text)
            else:
                ok_no = ["ok","no"]
                random.shuffle(ok_no)
                huh = [True,False]
                random.shuffle(huh)
                res_huh = random.choice(huh)
                res_ok_no = random.choice(ok_no)
                if res_huh == False:
                    if res_ok_no == "ok":
                        send=bot.reply_to(message, random.choice(RU.okay))
                        send
                        print("Ответ бота:",send.text)
                    else:
                        send=bot.reply_to(message, random.choice(RU.nope))
                        send
                        print("Ответ бота:",send.text)  
                else:
                    send=bot.reply_to(message, random.choice(RU.huh))
                    send
                    print("Ответ бота:",send.text)
        else:
            if ask in ENG.privet:
                bot.reply_to(message,random.choice(ENG.privet))

            elif "как дела" in ask or "как дела?" in ask:
                bot.reply_to(message,random.choice(ENG.dela))

            elif "кто ты?" in ask or "кто ты" in ask:
                bot.reply_to(message,random.choice(ENG.whoyou))

            else:
                ok_no = ["ok","no"]
                random.shuffle(ok_no)
                huh = [True,False]
                random.shuffle(huh)
                res_huh = random.choice(huh)
                res_ok_no = random.choice(ok_no)
                if res_huh == False:
                    if res_ok_no == "ok":
                        bot.reply_to(message, random.choice(ENG.okay))
                        
                    else:
                        bot.reply_to(message, random.choice(ENG.nope))

                else:
                    bot.reply_to(message, random.choice(ENG.huh))
@bot.message_handler(content_types=['document'])
def static_file(message):
    bot.send_message(message.chat.id, f"Название файла: {message.document.file_name}\nРазмер файла: {str(message.document.file_size)} Байтов\nТип файла: {str(message.document.mime_type)}")
    print(message.chat.first_name,"||",message.chat.username,"("+str(message.from_user.id)+")","File:")
    print(f"\nНазвание файла: {message.document.file_name}\nРазмер файла: {str(message.document.file_size)} Байтов\nТип файла: {str(message.document.mime_type)}")
bot.polling(none_stop=True, interval=0)