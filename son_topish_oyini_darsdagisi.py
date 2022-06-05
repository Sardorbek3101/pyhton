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
        if taxmin > tasodifiy_son:
            print("Men o'ylagan son bundan kichikroq. Yana harakat qiling")
        else:
            break
    return taxminlar
    print(f"Tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")