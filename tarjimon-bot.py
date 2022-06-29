import telebot
from googletrans import Translator
tarjimon = Translator()

TOKEN = "5485832305:AAFtcqI-K-mjz7K-Az2wQxGRbxp3oFBm8MA"

bot = telebot.TeleBot(TOKEN, parse_mode=None)   

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    bot.send_message(message.chat.id, f"Добро пожаловать, {javob}! \nНа какой язык"
    f"вы хотите переводить?\nЕсли на русский введите в начале текста (ru) || На английский напишите (en) ||узбекский (uz)", parse_mode="HTML")
    

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.startswith('en'):
        lan = 'en'
    elif msg.startswith('ru'):
        lan = 'ru'
    elif msg.startswith('uz'):
        lan = 'uz'
    else:
         bot.reply_to(message, 'Вы забыли отметить язык на которого нужно перевести (напишите "ru" "uz" или "en" в НАЧАЛЕ переводимого текста)')
    msgg = []
    for m in msg:
        msgg.append(m)
    del(msgg[0])
    del(msgg[0])
    while msgg[0] == ' ':
        del(msgg[0])
    messagee = ''
    for m in msgg:
        messagee += m
    
    javob = lambda messagee: tarjimon.translate(messagee , dest = lan)
    bot.reply_to(message, javob(messagee).text)

bot.infinity_polling()
