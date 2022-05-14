import telebot
import random
from gtts import gTTS
import qrcode


bot=telebot.TeleBot("5306980522:AAFmyDOeHsMYQI_LHH5reNmRXt1M2vB50ic")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username=message.from_user.first_name
    bot.reply_to(message,f"hello {username} wellcom ")

@bot.message_handler(commands=['game'])
def send_welcome(message):
    bot.reply_to(message,"Welcome to the game of guessing numbers")
    r=random.randint(0,50)
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        username=message.from_user.first_name
        d=int(message.text)
        if r==d:
            bot.reply_to(message,f"perfect {username} you win ")
        elif r<d:
            bot.reply_to(message,"go down")
        elif r>d:
            bot.reply_to(message," go up")

@bot.message_handler(commands=['voice'])
def send_seda(message):
    username=message.from_user.first_name
    bot.reply_to(message,f"hello {username} Welcome to the text-to-audio robot. Enter your text in English.")
    @bot.message_handler(func=lambda m:True)
    def echo(message):
        seda =gTTS(message.text)
        seda.save('seda.mp3')
        voice=open('seda.mp3','rb')
        bot.send_voice(message.chat.id,voice)

@bot.message_handler(commands =['age'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"hello {myname} Please enter your year of birth in solar:")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        sal = int(message.text)
        today = 1401 - sal
        bot.reply_to(message,f"{myname} You now {today} age!")
    
@bot.message_handler(commands =['qr'])
def send_a(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"please enter the text to convert qr cod")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        v = message.text
        img = qrcode.make(v)
        img.save("some_file.png")
        photo = open('some_file.png', 'rb')
        bot.send_photo(message.chat.id, photo)
@bot.message_handler(commands =['list'])
def list(message):
    myname = message.from_user.first_name
    list_num = []
    bot.reply_to(message,f"Enter a number in order to say the largest")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        if message.text != "/yes":
            num_lst =int(message.text)
            list_num.append(num_lst)
            max_lst = max (list_num)
        if message.text != "/yes":      
            bot.reply_to(message,f"The desired number was added to the list. If you run out of numbers,/startclick to")
        
        bot.reply_to(message,f"List of numbers you entered {list_num} :Is and its largest number \n {max_lst} Is")


            



# @bot.message_handler(commands=['fal'])
# def send_mesasge(mesasge):
#     fal_list=['love','sad',' trip','You will die']
#     fal=random.choice(fal_list)
#     bot.reply_to(mesasge,fal)

# @bot.message_handler(func=lambda m:True)
# def echo_all(message):
#     if message.text == "salam":
#         bot.reply_to(message,"hi ")
#     elif  message.text == "chtoryi":
#         bot.reply_to(message,"khobam ")

bot.infinity_polling()    