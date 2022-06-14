from uzwords import words
from transliterate import to_latin
import random as r

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

def play():
    while True:
        harflar = ('')
        soz = get_word()
        povtor_harf = (0)
        popitka = int(0)
        soz_uzunligi = len(soz)
        main = display('' , soz)
        print(f"Man {soz_uzunligi} xonali so'z o'yladim topa olasizmi?")
        print(main)
        while True:
            if povtor_harf == False:
                popitka += 1
            else:
                povtor_harf = (0)
            if popitka >= 2:
                harf = input("Agar to'liq sozni topgan bolsayz (+) ni bosing! \n1 ta harf kiriting: ").upper()
            else:
                harf = input("1 ta harf kiriting: ").upper()
            if harf == '+':
                harflar = ()
                harflar = input("Topgan so'zingizni kiriting agar xato topgan bo'lsangiz yutqazgan bo'lasiz ! \n>>>")
            elif len(harf) > 1:
                print("1 ta dan ko'p harf kiritish mukin emas")
            elif harf in harflar:
                print("Bu harfni avval kiritgan siz. Boshqa harf kiriting !")
                povtor_harf = 1
            else:
                harflar += harf+' '
                if harf in soz:
                    print(f"{harf} harfi to'g'ri !")
                else:
                    print("Bunday harf yo'q !")
            pole_chudes = display(harflar , soz)
            if harf == '+':
                break
            elif '-' in pole_chudes:
                print(pole_chudes)
                print(f"Shu vaqtgacha kiritgan harflaringiz: {harflar}")
            else:
                break    
        if harf == '+':
            if len(soz) != len(harflar):
                print(f"Afsuski siz yutqazdindiz, bu so'z {soz} edi")
            elif '-' in pole_chudes:
                print(f"Afsuski siz yutqazdindiz, bu so'z {soz} edi")
        else:
            print(f"Tabriklayman! {pole_chudes} so'zini {popitka} ta urinishda topdingiz !")
        restart = int(input("Yana o'ynaysizmi? / ha(1) yoq(0)"))
        if restart == False:
            break
