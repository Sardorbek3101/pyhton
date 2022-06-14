from uzwords import words
from transliterate import to_latin
import random as r
import telebot

def get_word():
    random_qiymat = r.choice(words)
    while '-' in random_qiymat or ' ' in random_qiymat:
        random_qiymat = r.choice(words)
    random_qiymat = to_latin(random_qiymat)
    return random_qiymat.upper()


def display(harflar, sozlar=get_word()):
    harflar = harflar.upper()
    tekshiruv = []
    togri_harflar = []
    pole = []
    pole_chudes = ('')
    x = {}
    for harf in harflar:        
        tekshiruv = harf in sozlar
        x[harf] = tekshiruv
    for w , v in x.items():
        if v == True:
            togri_harflar.append(w)
    for soz in sozlar:
        if soz in togri_harflar:
            pole.append(soz)
        else:
            pole.append('-')
    for pol in pole:
        pole_chudes += pol
    return pole_chudes

def play(msg):
    while True:
        harflar = ('')
        soz = get_word()
        returnn = ('')
        soz_harfi = []
        popitka = int(0)
        soz_uzunligi = len(soz)
        for f in soz:
            soz_harfi.append(f)
        main = display('' , soz)
        returnn += f"Man {soz_uzunligi} xonali so'z o'yladim topa olasizmi?\n{main}"
        while True:
            popitka += 1
            if popitka >= 2:
                returnn += "\nAgar to'liq sozni topgan bolsayz (+) ni bosing! \n1 ta harf kiriting: "
                if msg:          
                    harf = msg.upper()
            else:
                if msg:          
                    harf = msg.upper()
                returnn += "\n1 ta harf kiriting: "
            if harf == '+':
                harflar = ()
                returnn += "\nTopgan so'zingizni kiriting agar xato topgan bo'lsangiz yutqazgan bo'lasiz ! \n>>>"
                if msg: 
                    harflar = msg.upper()
            elif len(harf) > 1:
                returnn += "\n1 ta dan ko'p harf kiritish mukin emas"
            elif harf in harflar:
                returnn += "\nBu harfni avval kiritgan siz. Boshqa harf kiriting !"
            else:
                harflar += harf+' '
                if harf in soz:
                    returnn += f"\n{harf} harfi to'g'ri !"
                else:
                    returnn += "\nBunday harf yo'q !"
            pole_chudes = display(harflar , soz)
            if harf == '+':
                if '-' in pole_chudes:
                    break
            elif '-' in pole_chudes:
                returnn += f"\n{pole_chudes} \nShu vaqtgacha kiritgan harflaringiz: {harflar}"
            else:
                break    
            return returnn
        if '-' in pole_chudes:
            returnn += f"\nAfsuski siz yutqazdindiz, bu so'z {soz} edi"
        else:
            returnn += f"/nTabriklayman! {pole_chudes} so'zini {popitka} ta urinishda topdingiz !"
        return returnn
        restart = int(input("Yana o'ynaysizmi? / ha(1) yoq(0)"))
        if restart == False:
            break

TOKEN = "5458830568:AAFTSV_B6AXRGB4MZwwqNoh2XjfuuZWAZbg"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alaykum ! Hush kelipsiz!"
    javob += "\nHarf kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    bot.reply_to(message, play(msg))

bot.infinity_polling()


