import random as r
def odam_son_oylaydi():
    son = r.randint(1, 10)
    savol = ()
    taxmin = ()
    popitka = int()
    savol1 = ()
    savol2 = ()
    taxmin2 = ()
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
    print(popitka)
odam_son_oylaydi()