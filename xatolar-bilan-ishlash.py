#EXCEPTION
# =============================================================================
# yosh = input("Yoshingizni kirirting >>")
# try: #tekshiradi hato bormi , yoqmi
#     yosh = int(yosh)
# except ValueError: #AGAR ValueError degan xato chiqsa bu bajariladi , xoxlagan error ismini kiritish mumkin , kiritmasa ham bo'ladi - qanaqa hato bolsa ham ishla degani 
#     print("Butun son kiriting")
# else: #AGAR ERROR CHIQMASA BU BAJARILADI
#     print(f"Siz {2022 - yosh} - yilda tugulgan ekan siz")
#     
# print("Dastur davom emmoqda") #ERROR CHIQSA HAM DASTUR DAVOM ETADI
# =============================================================================
#ZeroDivisionError
# =============================================================================
# x , y = 5 , 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# =============================================================================
#IndexError
# =============================================================================
# mavalar = ['olma' , 'anor' , 'anjir' , 'uzum']
# try:
#     print(mavalar[4])
# except:
#     print("Ro'yxatda 4 ta meva bor xolos")
# =============================================================================
#KeyError
# =============================================================================
# user = {
#         'username' : 'Sardorbek',
#         "Status" : "Programmer",
#         'email' : "oscodeer@gmail.com",
#         "phone" : "+998949873858"
#         }
# key = "tel"
# try:
#     print(f"Foydalanuvchi {user[key]}")
# except:
#     print("Bunday kalit mavjut emas")
# =============================================================================
#FileNotFoundError
# =============================================================================
# filename = "data.txt"
# try:
#     with open(filename) as f:
#         text = f.read()
# except:
#     print(f"{filename} mavjut emas")
# =============================================================================
#pass
# =============================================================================
# import json
# files = ['talaba1.json' , 'talaba2.json' , 'talaba3.json' , 'talaba4.json']
# 
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass #Hech nima bjarmay prpustit qilip yuboradi
#     else:
#         print(talaba['ism'])
#         #fayl ustida turli amallar
# =============================================================================

# =============================================================================
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print('Butun son kiritmadingiz')
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# else:
#     print(f"x = {x}")
# =============================================================================

# =============================================================================
# while True:
#     yosh =  input("Yoshingizni kiriting")
#     if yosh.isdigit(): #isdigit - str ni ici sondan iboratmi tekshiradi
#         yosh = int(yosh)
#         break
# 
# print(f"Siz {2021 - yosh} da tugulgan siz")
# =============================================================================