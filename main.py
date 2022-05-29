# =============================================================================
# from python import * hamma narsani yuklab olish
# =============================================================================

# =============================================================================
# import python as py 
# 
# avto1 = py.avto_info('BMW', "X6", 'Black', 'Avtomat', 2021)
# print(avto1)
# 
# =============================================================================

# =============================================================================
# from python import avto_info as ainfo
# 
# avto1 = ainfo('BMW', "X6", 'Black', 'Avtomat', 2021)
# print(avto1)
# =============================================================================

# =============================================================================
# import math #matematik funktsiyalar
# x = 400
# print(math.sqrt(x)) #kvadrat ildizini hisoblaydi
# print(math.pow(5, 3)) #sonning malum bir darajasi
# print(math.pi) #pi ning qiymati
# print(math.log2(8)) 
# print(math.log10(100))
# =============================================================================
import random as r
son = r.randint(0, 100) #random son tanlash
print(son)
ismlar = ['ali' , 'vali' , 'hasan' , 'husan']
ism = r.choice(ismlar) #random qiymat tanlash
print(ism)
print(r.choice(ism)) #random harf tanlash

x = list(range(0,51,5))
print(x)
print(r.choice(x)) #random qiymat tanlash

x = list(range(11))
print(x)
r.shuffle(x) #sonlarni random aralashtirish
print(x)
