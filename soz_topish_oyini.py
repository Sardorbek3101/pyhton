from uzwords import words
import random as r

def get_word():
    random_qiymat = r.choice(words)
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
        soz_harfi = []
        popitka = int(0)
        soz_uzunligi = len(soz)
        for f in soz:
            soz_harfi.append(f)
        main = display('' , soz)
        print(f"Man {soz_uzunligi} xonali so'z o'yladim topa olasizmi?")
        print(main)
        while True:
            popitka += 1
            harf = input("Harf kiriting: ").upper()
            if harf in harflar:
                print("Bu harfni avval kiritgan siz. Boshqa harf kiriting !")
            else:
                harflar += harf
                if harf in soz:
                    print(f"{harf} harfi to'g'ri !")
                else:
                    print("Bunday harf yo'q !")
                pole_chudes = display(harflar , soz)
            if '-' in pole_chudes:
                print(pole_chudes)
                print(f"Shu vaqtgacha kiritgan harflaringiz: {harflar}")
            else:
                break
        print(f"Tabriklayman! {pole_chudes} so'zini {popitka} ta urinishda topdingiz !")
        restart = int(input("Yana o'ynaysizmi? / ha(1) yoq(0)"))
        if restart == False:
            break
