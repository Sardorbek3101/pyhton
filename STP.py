import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Men o'ylagan son bundan kattaroq. Yana harakat qiling")
        elif taxmin > tasodifiy_son:
            print("Men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc(x=10):
    taxminlar = 0
    input(f"1dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-)".lower())
        
        if javob == '+':
            quyi = taxmin + 1
        elif javob == '-':
            yuqori = taxmin-1
        else:
            break
    print("topdim")
    return taxminlar
def play(x=10):
    yana = 1
    while yana: 
        user_ball = sontop(x)
        pc_ball = sontop_pc(x)
        0
        if user_ball > pc_ball:
            print("Men yutdim")
        elif user_ball < pc_ball:
            print("Siz yutdiz")
        else:
            print("Durrang")
        yana = int(input("yana oynaysimi? ha(1) yoq(0)"))
