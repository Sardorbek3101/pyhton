#print(8/5)
#i = ("8/5 = " , 8//5)

#a = 5
#b = 6
#c = a * b
#print (c)

# name = 'sardor'
# surname = 'olimjonov'

# bla = (f"my name is {surname} {name}")


# print('hello \tworld')
# print('hello \nworld')

# print(bla.upper()) #lover()
# print(bla.title())
# print(bla.capitalize()) #lstrip() rstrip() strip() probelni olib tashlash

# ism = input("ismingiz nima?\n>>>")
# print("salamus " + ism.title())

# num = 12_485454_4545_5454_484
# print(num)

# a , b , c = 1 , 2 , 3
# print(a , b ,c)

# d = 100//2
# print(d)

# sui = 16
# bla = name + ' ' +  str(sui) + ' yoshda'
# print(bla)

# t_yil = int(input("tugulgan yilingizni kiriting pliiiz"))
# yosh = 2022 - t_yil
# print('siz ' , yosh , ' yosh da ekansiz')

#ILI
# t_yil = input("tugulgan yilingizni kiriting pliiiz")
# yosh = 2022 - int(t_yil)
# print('siz ' + str(yosh) + ' da ekansiz')
#name = 'Sardor'
#years = 16


# from queue import Empty
# from webbrowser import get


# a = int("20")
# b = float("20")
# c = str(20)

# mevalar = ["olma" , "anjir" , "shaftoli" , "o'rik"]
# narhlar = [12000 , 15000, 20000 , 250000 , 360000, -12 , 63.5]
# sonlar = ['bir' , 'iki' , 3 , 4 , 5]
# print(sonlar)
# print(mevalar)
# print(mevalar[0])
# print(mevalar[-1])
# print(mevalar[1].upper())
# print(narhlar[1] + narhlar[2])
# mevalar[0] = 'anor'
# mevalar[-1] = 'uzum'
# print(mevalar)

# mevalar.append('tarvuz')
# print(mevalar)
# mevalar.insert(0 , 'banan')
# mevalar.insert(3, 'ananas')
# print(mevalar)

#cars = []
#cars.append('lacetti')
#cars.append('nexia')
#cars.append('matiz')
#cars.append('tico')
# print(cars)
# del(cars[0])
# print(cars)
# cars.remove('tico')
# print(cars)

# animals = ['it' , 'mushuk' , 'sigir' , 'mushuk']
# print(animals)
# animals.remove('mushuk')
# print(animals)

# bozorlik = ['piyoz' , 'kartoshka' , "go'sht" , 'un']
# print(bozorlik)
# mahsulot = bozorlik.pop(1)
# print(mahsulot)
# print(bozorlik)

# print('man' , mahsulot , 'sotib oldim')
# print('olinmagan mahsulotlar:' , bozorlik)

# .sort() = alfavit boyicha tartiblash
# .sort(reverse=True) = alfavit boyicha teskari tartiblash
# sorted = alfavit boyicha sozlash ozgaruvchini ozgarmasdan 
# print(sorted(cars))
# print(sorted(cars , reverse=True)) = alfavit boyicha teskari tartiblash ozgaruvchini ozgarmasdan 
# tepadagilar sonlarda ham ishlaydi
# .reverse() = elementlarni teskari joylash = masalan : bmw , audi = audi , bmw
# len(cars) = elementlarni sonini aniqlash
#sonlarr = list(range(0,10))
#toq_sonlar = list(range(1 , 19 , 2))
#juft_sonlar = list(range(0 , 18 , 2))
#sanash = list(range(0 , 101 , 10))

#narhlar = [15000 , 50000 , 42000 , 78000 , 63000]
#print(max(narhlar))
#print(min(narhlar))
#print(sum(narhlar))
#print("narhlar" , min(narhlar) , "sum dan boshlanib" , max(narhlar) , "sum gacha , obshi", sum(narhlar) , "sum" )
#print(cars[2:3])
#print(cars[:2])
#print(cars[2:])
# agar my_cars = cars degan komanda bersak bitta elementda 2 ta nom bergan bolamiz : cars i my_cars
# agar cars dan nusqa olmoqchi bolsak bu komandadan foydalanamiz "my_cars = cars[:]"

# ozgarmas list
#my_hobby = ("footbal" , "tennis" , "backedball" , "hokkey" , "box")
#my_hobby.append("judo") = error   
#my_hobby = list(my_hobby)
#my_hobby.append("judo")
#print(my_hobby)
#my_hobby = tuple(my_hobby)

#avtolar = ['audi', 'bmw' , 'volvo' , 'kia' , 'hyundai']
#for avto in avtolar :
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())

#.lower = katta va kichik harflar bir hil

# =============================================================================
# ism = input("ismingizni nima? \n>>>")
# if ism.lower() != "ali":
#     print(f"uzur {ism} biz Alini kutyappiz")
# else:
#     print("Salom , Ali")
# =============================================================================

# =============================================================================
# javob = float(input("12*6 nechiga teng? \n>>> "))
# if javob != 72:
#     print("javob xato")
# else:
#     print("javob tug'ri")
# =============================================================================

# =============================================================================
# yosh = int(input("yoshingiz nechida? \n>>> "))
# if yosh >= 18:
#     print("xush kelipsiz")
# else:
#     print("kirish mukinn emas")
# =============================================================================

# =============================================================================
# login = input("Yangi login tanlang!")
# if len(login) <= 5:
#     print("login 5 harfdan koproq bolishi shart")
# =============================================================================

# =============================================================================
# yil = int(input("tugulgan yilingizni kiriting \n>>> "))
# if 2022-yil < 18:
#     print(f"yoshingiz {2022-yil} da ekan")
#     print("kirish mumkin emas")
# else:
#     print("Xush kelipsiz!")
# =============================================================================

# =============================================================================
# yoshh = int(input("yoshingiz nechida? >>>>"))
# if yoshh > 65: print("Siz COVID-19 risk guruhida ekansiz")
# =============================================================================

#if va else operatorlarini bir qatorda yozish uslubi
# =============================================================================
# x , y = 25 , 50
# print("x>y") if x>y else print("x<y")
# =============================================================================
