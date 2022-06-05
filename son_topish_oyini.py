import random as r
print("Keling o'ylagan sonni topish o'ynaymiz!")
while True:
    bot_oylagan_son = int(r.randint(1, 10))
    popitkaa = int(0)
    taxminn = int(input(f"1 dan {10} gacha son o'yladim topa olasizmi? : \n>>"))
    while True:
        popitkaa += 1
        if(taxminn > bot_oylagan_son):
            taxminn= int(input("Xato , men o'ylagan son bundan kichikroq. Yana harakat qiling: \n>>"))
        elif(taxminn < bot_oylagan_son):
            taxminn= int(input("Xato , men o'ylagan son bundan kattaroq. Yana harakat qiling: \n>>"))
        else:
            print(f"TOPDINGIZ! {bot_oylagan_son} sonini oylagan edim. {popitkaa} ta taxmin bilan topdingiz. Tabriklayman!")
            break
#2Часть
    savol = ()
    taxmin = ()
    popitka = int(0)
    savol1 = ()
    savol2 = ()
    taxmin2 = ()   
    son = r.randint(1, 10)
    print("\n1 dan 10 gacha son o'ylang. Man topishga harakat qilaman")
    input("Son oylagan bo'lsangiz istalgan tugmani bosing.")
    while savol != 'T'.lower():
        popitka += 1
        if popitka >=2:
            while savol != 'T'.lower():
                popitka += 1
                if (savol1 == '+' and savol2 == '-'):
                    taxmin2 = r.randint(son + 1, taxmin - 1)
                    savol3 = input(f"Siz {taxmin2} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                    savol = savol3[:]
                if (savol1 == '-' and savol2 == '+'):
                    taxmin2 = r.randint(taxmin + 1, son - 1)
                    savol3 = input(f"Siz {taxmin2} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                    savol = savol3[:]
                if (savol1 == '-' and savol2 == '-'):
                    taxmin2 = r.randint(1, taxmin -1)
                    savol3 = input(f"Siz {taxmin2} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                    savol = savol3[:]
                if (savol1 == '+' and savol2 == '+'):
                    taxmin2 = r.randint(taxmin + 1, 10)
                    savol3 = input(f"Siz {taxmin2} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                    savol = savol3[:]
                if popitka >= 3:
                    son = taxmin
                    taxmin = taxmin2
                    savol1 = savol2
                    savol2 = savol3
        else:
            savol1 = input(f"Siz {son} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
            savol = savol1[:]
            if savol1 == '+':
                taxmin = r.randint(son + 1, 10)
                savol2 = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                savol = savol2[:]
            elif savol1 == '-':
                taxmin = r.randint(1, son - 1)
                savol2 = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (T), man o'ylagan son bundan kattaroq (+) , yoki kichikroq(-) ??")
                savol = savol2[:]
    print(f"\nSoningizni {popitka} ta taxmin bilan topdim!")  
    if popitkaa < popitka:
        print(f"Siz {popitkaa} ta taxmin bilan toptiz va yuttingiz!")
    elif popitkaa > popitka:
        print(f"Siz {popitkaa} ta taxmin bilan toptiz va yutqazdingiz")
    else:
        print(f"Durrang! Ikkimiz ham {popitka} bilan topdik!")
    javob = int(input("yana oynaysimi? ha(1) yoq(0)"))
    if(javob == 0):
        break

