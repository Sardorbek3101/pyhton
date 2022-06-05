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

# =============================================================================
# yosh = int(input("yoshingiz nechida? >>>"))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} summ")
# =============================================================================

# =============================================================================
# kun = input("bogun nima kun? >>>")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni!")
# else:
#     print("Bugun ish kuni!")
# =============================================================================

# =============================================================================
# kunn = input("bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>> "))
# 
# if (kunn.lower() == 'yakshanba' or kunn.lower() == 'shanba') and harorat >= 30:
#     print('Chomilgani ketdik!')
# elif (kunn.lower() == 'yakshanba' or kunn.lower() == 'shanba') and harorat < 30:
#     print('Uyda dam olamiz!')  
# else:
#     print('bugun ish kuni!')
# =============================================================================

# =============================================================================
# narh = 15000
# choy = True
# salat = False
# 
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
# print(f"jami {narh} sum")
# =============================================================================

# =============================================================================
# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# asorti = False
# 
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if asorti:
#     print("Mijoz asorti oldi.")
#     narh = narh + 15000
# print(f"Jami {narh} sum")
# =============================================================================
    
# =============================================================================
# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# asorti = 1
# 
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if asorti:
#     print("Mijoz asorti oldi.")
#     narh = narh + 15000
# print(f"Jami {narh} sum")
# =============================================================================

# =============================================================================
# menu = ['osh' , 'qazonkabob' , 'shashlik' , 'norin' , 'somsa']
# #'somsa' in menu #menu da somsa bormi?
# ovqat = input("nima ovqat yeysiz> >>>")
# if ovqat in menu:
#     print("buyurtma qabul qilindi")
# else:
#     print('afsuzki bizda bunday ovqat yo\'q')
# =============================================================================

# =============================================================================
# menu = ['osh' , 'qazonkabob' , 'shashlik' , 'norin' , 'somsa']
# #'somsa' not in menu #menu da somsa yoqmi?
# ovqat = input("nima ovqat yeysiz> >>>")
# if ovqat not in menu:
#      print('afsuzki bizda bunday ovqat yo\'q')
# else:
#      print("buyurtma qabul qilindi")
# =============================================================================
# 2 ta ozgaruvchilarni solishtirish
# =============================================================================
# menu = ['osh' , 'qazonkabob' , 'shashlik' , 'norin' , 'somsa']
# buyurtmalar = ['osh' , 'somsa' , 'manti' , 'shashlik']
# if buyurtmalar:
#     print(f"buyurtmalarda {len(buyurtmalar)} taom bor")
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"menu da {taom} bor")
#         else:
#             print(f"Kechirasiz menu da {taom} yoq")
# else:
#     print("ro'yxat bo'sh")
# =============================================================================

# =============================================================================
# car = {'model' : 'Ferrari' , 'color' : 'red'}
# print(car['model'])
# print(car['color'])
# =============================================================================

# =============================================================================
# en_uz = {'apple' : 'olma' , "apricot" : "o'rik" , 'banana' : 'banan' }
# print(en_uz['banana'])
# print(en_uz)
# =============================================================================

# =============================================================================
# student = {'name' : 'olimjonov sardorbek' , 'yil' : '2006' , 'yosh' : '16'}
# print(f"{student['name'].title()} , {student['yil']} yil da tugulgan , hozir {student['yosh']}")
# 
# student['kurs'] = 1
# student['fakulted'] = 'informatika'
# student['name'] = 'olimjonov sardor'
# print(student)
# del student['yosh']
# print(student)
# =============================================================================

# =============================================================================
# telefonlar = {
#      'ali' : 'iphone x',
#      'vali' : 'iphone 11',
#      'gani' : 'iphone 12 pro',
#      'gayrat' : 'iphone 13 pro max',
#      'gari' : 'samsung s21 ultra'    
#     }
# print(telefonlar)
# 
# print(telefonlar.get('username' , 'bunday user mavjut emas')) #bu informasiya berishda ishlatilinadi
# =============================================================================

# =============================================================================
# student = {'name' : 'olimjonov sardorbek' , 'yil' : '2006' , 'yosh' : '16'}
# print(student.items())
# for kalit , qiymat in student.items():
#     print(f"kalit = {kalit}")
#     print(f"qiymat = {qiymat}\n")
# =============================================================================

# =============================================================================
# telefonlar = {
#      'ali' : 'iphone x',
#      'vali' : 'iphone 11',
#      'gani' : 'iphone 12 pro',
#      'gayrat' : 'iphone 13 pro max',
#      'gari' : 'samsung s21 ultra'    
#     }
# for k , q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
# =============================================================================

# =============================================================================
# telefonlar = {
#      'ali' : 'iphone x',
#      'vali' : 'iphone 11',
#      'gani' : 'iphone 12 pro',
#      'gayrat' : 'iphone 13 pro max',
#      'gari' : 'samsung s21 ultra'    
#     }
# print(telefonlar)
# print(telefonlar.keys()) #kalit so'zlarni ajratib olish
# for tel in telefonlar:
#     print(tel.title())
# =============================================================================

# =============================================================================
# mahsulotlar = {
#     'olma' : 10000,
#     'anor' : 20000,
#     'uzum' : 40000,
#     'anjir' : 25000,
#     'shaftoli' : 30000
#     }
# bozorlik = ['anor' , 'uzum' , 'non' , 'baliq']
# 
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
# 
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'konizga {buyum} ham olip keling")
# 
# for mahsulot in sorted(mahsulotlar):
#     print(f"\n{mahsulot.title()}")
# =============================================================================

# =============================================================================
# telefonlar = {
#      'ali' : 'iphone x',
#      'vali' : 'iphone 11',
#      'gani' : 'iphone 12 pro',
#      'gayrat' : 'iphone 13 pro max',
#      'gari' : 'samsung s21 ultra'    
#     }
# #print(telefonlar.values()) #telefonlar ro'yxatini qiymatlari
# 
# for telefon in telefonlar.values():
#     print(telefon.title())
# =============================================================================
    
# =============================================================================
# telefonlar = {
#      'ali' : 'iphone x',
#      'vali' : 'iphone 11',
#      'gani' : 'iphone 12 pro',
#      'gayrat' : 'iphone 13 pro max',
#      'gari' : 'samsung s21 ultra', 
#      'tohir' : 'iphone x',
#      'shodi' : 'iphone x',
#      'tesha' : 'iphone 13 pro max',
#      'ketmon' : 'iphone 13 pro max'
#     }
# #set() - qayta qayta kelayotkan qiymatlarni 1 tadann qoldiradi
# print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar")
# for telefon in set(telefonlar.values()):
#     print(telefon.title())
# =============================================================================

# =============================================================================
# toys = {'ball' , 'car' , 'lamp' , 'ball' , 'bear' , 'car'} #type - set qaytarilgan qiymatni bittasini korsatadi
# print(toys)
# =============================================================================

#NESTING
# =============================================================================
# car0 = {
#         'model' : 'lacetti',
#         'rang' : 'oq',
#         'yil' : 2018,
#         'narh' : 13000,
#         'km' : 50000,
#         'korobka' : 'avtomat'
#         }
# car1 = {
#         'model' : 'nexia 3',
#         'rang' : 'qora',
#         'yil' : 2015,
#         'narh' : 9000,
#         'km' : 89000,
#         'korobka' : 'mexanika',
#         }
# car2 = {
#         'model' : 'gentra', 
#         'rang' : 'qizil',
#         'yil' : 2015,
#         'narh' : 9000,
#         'km' : 89000,
#         'korobka' : 20000,
#         }
# 
# cars = [car0 , car1 , car2]
# for car in cars:
#     print(f"{car['model'].title()} , "
#           f"{car['rang']} rang , "
#           f"{car['yil']}-yil , {car['narh']}$ "
#           )
# print(cars[0]['model'])
# print(cars[2]['rang'] , cars[2]['model'])
# =============================================================================

# =============================================================================
# malibus = []
# for n in range(10):
#     new_car = {
#             'model' : 'malibu', 
#             'rang' : None,
#             'yil' : 2022,
#             'narh' : None,
#             'km' : 0,
#             'korobka' : 'avto',
#             }
#     malibus.append(new_car)
# 
# #for malibu in malibus:
# #    print(malibu)
# 
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
#     
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
#     
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
#     
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000
#         
# for malibu in malibus :
#     print(malibu)
# =============================================================================

# =============================================================================
# dasturchilar = {
#     'ali' : ['python' , 'c++'],
#     'vali' : ['html' , 'css' , 'js'],
#     'hasan' : ['php' , 'sql'],
#     'husan' : ['python' , 'php'],
#     'maryam' : ['c++' , 'c#'],
#     }
# # =============================================================================
# # for ism , tillar in dasturchilar.items():
# #     print(f"\n{ism.title()} quyidgi dasturlash tilini biladi:")
# #     for til in tillar:
# #         print(til.upper())
# # =============================================================================
#         
# for ism , tillar in dasturchilar.items():
#     print(f"\n\n{ism.title()} quyidgi dasturlash tilini biladi:")
#     for til in tillar:
#         print(til.upper() , end = ' ')
# =============================================================================

# =============================================================================
# hamkasblar = {
#     'ali' : {'familiya' : 'valiyev',
#              'tyil' : 1995,
#              'malumot' : 'oliy',
#              'tillar' : ['python' , 'c++']
#         } ,
#     'vali' : {'familiya' : 'aliyev',
#              'tyil' : 2001,
#              'malumot' : "o'rta-maxsus",
#              'tillar' : ['html' , 'css' , 'js']
#         },
#     'hasan' : {'familiya' : 'husanov',
#              'tyil' : 1999,
#              'malumot' : 'maxsus',
#              'tillar' : ['python' , 'php']
#         } 
#     }
# for ism , info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()} ,\n"
#           f"{info['tyil']}-yil da tug'ilgan , "
#           f"malumoti {info['malumot']}.\n"
#           f"Quyidagi dasturlash tillarini biiladi : ")
#     for til in info['tillar']:
#         print(til.upper())
# 
# =============================================================================
#primer
# =============================================================================
# primer = int(input('6*6 = ?'))
# if primer == 6 * 6:
#     print('velkome')
# else:
#     print('error')
# 
# =============================================================================

# =============================================================================
# ism = input('ismingiz nima?')
# savol = f"Salom {ism.title()} yoshingiz nechida?"
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Boyingiz nechida?")
# height = float(height)
# =============================================================================

# =============================================================================
# son = 1
# while son <= 5:
#     print(son , end = ' ')
#     son += 1
# print('dastur tugadi')
# =============================================================================

# =============================================================================
# print('Kiritilgan sonni kvadratini chiqaruvchi dastur !')
# savol = 'Istalgan son kiriting '
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing) :"
# qiymat = ''
# while  qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
# print('Dastur tugadi.')
# =============================================================================

# =============================================================================
# print('Kiritilgan sonni kvadratini chiqaruvchi dastur !')
# savol = 'Istalgan son kiriting '
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing) :"
# qiymat = ''
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print('Dastur tugadi.')
# =============================================================================

# =============================================================================
# print('Kiritilgan sonni kvadratini chiqaruvchi dastur !')
# savol = 'Istalgan son kiriting '
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing) :"
# qiymat = ''
# while True: #abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break #tsikilni to'xtatish
#     else:
#         print(float(qiymat) ** 2)
# print('Dastur tugadi.')
# =============================================================================

# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break #toxtatish
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
# =============================================================================
    
# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue #kodni boshidan davom etish
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
# =============================================================================

# =============================================================================
# son = 0
# while son < 10:
#     son += 1
#     if son %2 != 0:
#         continue
#     else:
#         print(son)
# =============================================================================

# =============================================================================
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# 
# while True:
#     savol = f"{n} do'stingizni izmini kiriting :"
#     ism = input(savol)
#     ismlar.append(ism)
#     n += 1
#     takrorlash = input("yana ism qoshasizmi ? (ha/yoq')")
#     if takrorlash.lower() != 'ha':
#         break
# 
# print("Do'stlaringiz ro'yhati")
# for ismm in ismlar:
#     print(ismm.title())
# =============================================================================
    
# =============================================================================
# dostlar = {}
# ishora = True
# 
# while ishora:
#     ism = input("Do'stingizni ismini kiriting : ")
#     yosh = input(f"{ism.title()}ning yoshi nechida ? ")
#     dostlar[ism] = int(yosh)
#     
#     javob = input("Yana malumot qo'shasizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False
#     
# for ism , yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
# =============================================================================

# =============================================================================
# cars = ['lacetti' , 'nexia' , 'toyota' , 'nexia' , 'audi' , 'malibu' , 'nexia']
# 
# while 'nexia' in cars :
#     cars.remove('nexia')
# print(cars)
# =============================================================================

# =============================================================================
# talabalar = ['hasan' , 'husan' , 'ali' , 'vali' , 'gayrat']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting : ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba.title()] = int(baho)
# print(talabalar)
# print(baholangan_talabalar)
# =============================================================================

#FUNCTION
# =============================================================================
# def salom_ber():
#     """salom beruvchi funktsiya""" #DOCSTRING - funktsiya haqida malumot  berish
#     print("Asalom Alaykum")
# 
# #salom_ber()
# 
# def kutib_ol(ism):
#     """Foydalanuvchining ismini qabul qilib ,
#     unga salom beruvchi funktsiya"""
#     print(f"Assalomu alaykum , hurmatli {ism.title()}")
# 
# kutib_ol('Sardorbek')
# 
# print(kutib_ol.__doc__) #Funktsiya haqida malumot olish
# print(print.__doc__)
# =============================================================================

# =============================================================================
# def toliq_ism(ism , familiya):
#     """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funktsiya"""
#     print(f"\nFoydalanuvchi ismi : {ism.title()}\n"
#           f"Foydalanuvchi familyasi : {familiya.title()}")
# 
# toliq_ism('Sardorbek', 'Olimjonov')
# toliq_ism(familiya = 'Kamolov',ism = 'Ruslan')
# 
# def yoshni_hisobla(ism , t_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2022 - t_yil} yoshda")
#     
# yoshni_hisobla('Sardorbek', 2006)
# yoshni_hisobla(t_yil=2006, ism = 'Ruslan')
# =============================================================================

# =============================================================================
# def yosh_hisobla(tugulgan_yil , joriy_yil = 2022):
#     """Foydalanuvchi tugulgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugulgan_yil} yosh da siz")
# 
# yosh_hisobla(2006 , 2023)
# yosh_hisobla(2006)
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism , familiya):
#     """to'liq ism qaytaruvchi funktsiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# 
# talaba = toliq_ism_yasa('sardor', 'olimjonov') #funktsiya dagi qiymatni ozgaruvchiga solish
# print(talaba)
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism , familiya , otasining_ismi = ''):
#     """to'liq ism qaytaruvchi funktsiya"""  
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#     
# talaba1 = toliq_ism_yasa('Sardorbek', 'Olimjonov')
# talaba2 = toliq_ism_yasa('ruslan', 'kamolov' , 'rustamovich')
# print(f"Darsga kelmagan talabalar : {talaba1} va {talaba2}")
# =============================================================================

# =============================================================================
# def avto_info(kompania , model , rangi , korobka , yili , narhi = None):
#     avto = {'kompania' : kompania ,
#           'model' : model,
#           'rangi' : rangi,
#           'korobka' : korobka,
#           'yil' : yili,
#           'narh' : narhi
#           }
#     return avto
# 
# avto1 = avto_info('Gm','Malibu', 'Qora', 'Avtomat', '2018')
# avto2 = avto_info('Gm', 'Gentra', 'Oq', 'Mexanika', '2016' , 15000)
# 
# avtolar = [avto1 , avto2]
# #print(avtolar[1]['model'])
# print("Onlayn bozorda mavjut avtomashinalar : ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "noma'lum"
#     print(f"{avto['rangi']} {avto['model']} narhi : {narh}")
# 
# =============================================================================
# =============================================================================
# def oraliq(min , max , qadam = 1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         if qadam:
#             min += qadam
#     return sonlar
# print(oraliq(1, 21))
# print(oraliq(0, 1010 , 10))
# =============================================================================

# =============================================================================
# def avto_info(kompania , model , rangi , korobka , yili , narhi = None):
#     avto = {'kompania' : kompania ,
#           'model' : model,
#           'rangi' : rangi,
#           'korobka' : korobka,
#           'yil' : yili,
#           'narh' : narhi
#           }
#     return avto
# print("Salonimizdagi atolarro'yxatini shakillantiramiz.\n")
# avtolar=[]
# 
# while True:
#     print("Quyidagi malumotlarni kiriting")
#     kompania = input("Ishlab chiqaruvchi : ")
#     model = input("Modeli : ")
#     rangi = input('Rangi : ')
#     korobka = input('Koropkasi : ')
#     yili = input("Ishlab chiqarilgan yili : ")
#     narhi = input("Narhi : ")
#     
#     avtolar.append(avto_info(kompania, model, rangi, korobka, yili , narhi))
#     
#     javob = input("Yana avto qo'shasizmi ? (yes/no)")
#     if javob == 'no':
#         break
#     
# print("\nSaloningizdagi avtolar : ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "noma'lum"
#     print(f"{avto['rangi']} {avto['model']} narhi : {narh}")
# =============================================================================

# =============================================================================
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} bahosini kiriting : ")
#         baholar[ism] = baho
#     return baholar
# 
# talabalar = ['ali' , 'vali' , 'hasan' , 'husan']
# baholar = bahola(talabalar[:]) #[:] bu qiymatni kopiyasini olishga yordam beradi
# print(baholar)
# print(talabalar)
# =============================================================================
        #args
# =============================================================================
# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# 
# print(summa(1,2,3,4,5))
# print(summa(15,25,85))
# 
# def suma(x , y , *sonlar):
#     return x+y+sum(sonlar)
# 
# print(suma(1,2,5))
# =============================================================================
        #**kwargs
# =============================================================================
# def avto_info(kompaniya , model , **malumotlar):
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# 
# avto1 = avto_info('GM', 'malibu', rang = 'qora' , yil = 2018)
# avto2 = avto_info('Kia', 'K5', rang = 'qizil' , narh = 35000 , yil = 2020 , korobka = 'avomat')
# print(avto1 , avto2)
# =============================================================================

#NOMSIZ FUNKTSIYALAR

# =============================================================================
# kvadrat = lambda x,y :x**y
# print(kvadrat(3, 2))
# =============================================================================

# =============================================================================
# def daraja(n):
#     return lambda x : x*n
# 
# x2 = daraja(2)
# kub = daraja(3)
# 
# print(f"3-ni 2 ga kupayytirsa {x2(3)} ga , " 
#       f"kubi {kub(3)} ga teng") 
# =============================================================================

# =============================================================================
# from math import sqrt #kvadrat ildiz hisoblaydigan funktsiya
# 
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar)) # map - har bir list qiymatiga funktsiyani qollaydi
# #print(ildizlar)
# 
# def daraja2(x):
#     """berilgan sonning kvadratini qaytaruvchi funktsiya"""
#     return x*x
# 
# #print(daraja2(3))
# print(list(map(daraja2, sonlar)))
# 
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)
# =============================================================================

# =============================================================================
# a = [4 , 5 , 6]
# b = [7 , 8 , 9]
# a_plus_b = list(map(lambda x , y : x + y, a , b))
# print(a_plus_b)
# =============================================================================

# =============================================================================
# import random as r
# 
# sonlar = list(r.sample(range(100), 10))
# 
# def juftmi(x):
#     """x juft son bolsa True , aks holda False qaytaruvchi funktsiya"""
#     return x%2 == 0
# 
# #print(juftmi(3))
# 
# # =============================================================================
# # juft_sonlar = list(filter(juftmi, sonlar))
# # print(juft_sonlar)
# # =============================================================================
# 
# juft_sonlar = list(filter(lambda son: son%2 == 0, sonlar))
# print(juft_sonlar)
# =============================================================================

# =============================================================================
# mevalar = ['olma' , 'anor' , 'anjir' , 'shaftoli' , "o'rik" , 'tarvuz' , 'qovun' , 'banan']
# harf = 'b'
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# #print(mevalar_b)
# 
# mevalar2 = list(filter(lambda meva: len(meva)<=5, mevalar))
# print(mevalar2)
# 
# anor = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# print(anor)
# =============================================================================
    