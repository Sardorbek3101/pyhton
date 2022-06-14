#Tavsiya qilinmaydigan uusul
# =============================================================================
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()
# =============================================================================
#TAVSIYA QILINGN USUL
# =============================================================================
# with open('pi.txt') as file:
#     pi = file.read()
#     
# 
# pi = pi.rstrip()
# pi = pi.replace('\n', '')
# pi = float(pi)
# print(type(pi))
# print(pi)
# =============================================================================

# =============================================================================
# filename = 'data/talabalar.txt'
# # =============================================================================
# # with open(filename) as file:
# #     for line in file:
# #         print(line)
# # =============================================================================
# with open(filename) as file:
#     talabalar = file.readlines()
#     
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)
# =============================================================================
#TXT fayliga 0 dan qiymat kiritish
# =============================================================================
# filename = "new_file.txt"
# ism = "Sardorbek Olimjoov"
# tyil = 2006
# with open(filename , 'w') as file:
#     file.write(ism + '\n')
#     file.write(str(tyil) + '\n')
# =============================================================================
#TXT fayliga qiymat qo'shish
# =============================================================================
# filename = "new_file.txt"
# with open(filename , 'a') as file:
#     file.write('Programmer\n')
# =============================================================================
#O'ZGARUVCHI, LUGAT, FUNKTSIYA va qolgan python da ishlatiladigan narsalarni faylga joylash usuli
# =============================================================================
# import pickle
# 
# talaba1 = {'ism':'hasan' , 'familiya' : 'husanov' , 'tyil' : 2003 ,'kurs' : 2}
# talaba2 = {'ism':'alijon' , 'familiya' : 'valiyev' , 'tyil' : 2004 ,'kurs' : 1}
# 
# with open('info' , 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
# =============================================================================
#O'ZGARUVCHI, LUGAT, FUNKTSIYA va qolgan python da ishlatiladigan narsalarni fayldan olish , o'qish usuli
# =============================================================================
# import pickle
# 
# with open('info' , 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
#     
# print(talaba1 , talaba2)
# =============================================================================
