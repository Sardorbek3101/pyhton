#DATETIME
# =============================================================================
# import datetime as dt
# 
# hozir = dt.datetime.now() #hozirgi chislo va soatni korsatadi
# print(hozir)
# print(hozir.date()) #bugungi chisloni ko'rsatadi
# print(hozir.time()) #hozirgi vaqti ko'rsatadi
# print(hozir.hour) #hozir soat nechiligini ko'rsatadi
# print(hozir.minute) #soatni minutini ko'rsatadi
# print(hozir.second) #minutni sekundini ko'rsatadi
# 
# bugun = dt.date.today() #bugungi sanani ko'rastadi
# print(f"Buguni sana:{bugun}")
# erta = dt.date(2022, 6, 23) #ozimiz vaqt beramiz
# print(f"Ertangi sana: {erta}")
# 
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time() #hozirgi vaqtni ko'rsatadi
# print(vaqtHozir)
# vaqtKeyin = dt.time(15 , 45 , 50) #o'zimiz vaqt beramiz
# print(vaqtKeyin)
# 
# #SANALAR RASIDA FARQ
# 
# bugun = dt.date.today()
# tugulgan_kun = dt.date(2023, 1, 31)
# farq = tugulgan_kun - bugun
# print(f"Tugulgann kunimga {farq.days} kun qoldi")
# 
# hozir = dt.datetime.now()
# futbol = dt.datetime(2022, 6, 23 , 22 , 15 , 00)
# farq = futbol - hozir
# #print(farq)
# sekundlar = farq.seconds
# minutlar = sekundlar//60
# soat = minutlar//60
# print(f"futbolgacha {farq.days} kun {soat} soat qoldi")
# =============================================================================
#pprint
# =============================================================================
# from pprint import pprint
# import json
# 
# # =============================================================================
# # filename = 'bemor.json'
# # with open(filename) as  f:
# #     bemor = json.load(f)
# # #print(bemor)
# # pprint(bemor) #pprint - MALUMOTLARNI CHIROYLI QILIP CHIQARISH
# # =============================================================================
# 
# import requests
# 
# r = requests.get('https://api.github.com')
# 
# pprint(r.json())
# =============================================================================
#ANDOZA
# =============================================================================
# import re
# from uzwords import words
# # =============================================================================
# # word1 = 'темир'
# # word2 = 'томир'
# # word3 = 'тулпор'
# # 
# # andoza = '^т...р$'#kalit so'z
# # 
# # print(re.match(andoza , word1)) #kalit so'z orqali ajratib olish
# # print(re.match(andoza , word2)) #kalit so'z orqali ajratib olish
# # print(re.match(andoza , word3)) #kalit so'z orqali ajratib olish
# # =============================================================================
# 
# # =============================================================================
# # andoza = '^а...р$' #kalit so'z
# # matches = []
# # for word in words:
# #     if re.match(andoza, word):#kalit so'z orqali ajratib olish
# #         matches.append(word)
# # print(matches)
# # =============================================================================
# 
# # =============================================================================
# # kalit = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# # tayor_kalit_suzlar = 'https://ihateregex.io/'
# # 
# # text = 'Тех. поддержка: Бухгалтерия: Руководство: Telegram: Skype: support@beget.com bills@beget.com manager@beget.com @begetbot Добавить в контакты Россия: СПб: Москва: Украина: Киев: +7 (800) 700-06-08 +7 (812) 3854136  +7 (495) 721-80-88 +380 (800) 802-192 +380 (44) 300-02-18'
# # 
# # email = re.findall(kalit, text) #re.findall() - text ichida kalit bilan belgilanga so'zlarni ajratib olish
# # print(email)
# # =============================================================================
# 
# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# 
# msg = "Yangi parol kiriting (kamida 8 ta belgidan ibora , va kamida 1 ta katta lotin harf , 1 ta kichik lotin harf , 1 ta son va 1 ta maxsus belgi bo'lishi shart)"
# 
# while True:
#     password =  input(msg)
#     if re.match(andoza, password):
#         print("Maxviy so'z qabul qilindi")
#         break
#     else:
#         print("Maxviy soz talabga javob bermadi")
# =============================================================================
