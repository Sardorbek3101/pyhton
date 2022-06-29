# =============================================================================
# import unittest #Test qilish uchun kerakli funktsiyani import orqali olinadi
# from name import get_full_name #Test qiladigan funktsiyamizni import qilamiz
# 
# class NameTest(unittest.TestCase): #test qilish uchun (unittest.TestCase) - deyarli faqat shu ishlatilinishi uchun shunday merosli class yaratamiz
#     def test_get_name(self): #testni funktsiyanini yaratamiz (test)BILAN BOSHLANISHI SHART!
#         name = get_full_name('sardorbek', 'olimjonov') #funktsiyaga sinov uchu qiymat beramiz
#         self.assertEqual(name , 'Sardorbek Olimjonov') #Kerakli qiymat ga to'gri keladimi yoqmi tekshiramiz
#     
#     def test_otasi(self):
#         otasi = get_full_name('sardorbek', 'olimjonov' , 'olimjonovich')
#         self.assertEqual(otasi, 'Sardorbek Olimjonovich Olimjonov')
#         
# unittest.main() #Testni boshlaymiz
# =============================================================================

import unittest
from name import get_area , get_perimeter

class Get_test(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(get_area(5),78.53975) #assertAlmostEqual - deyarli teng bo'lsa ||self.assertAlmostEqual(get_area(5),78.53975 , 4) - nuqtadan keyingi 4 xonali son gacha aniq bo'sin qolgani shart emas
        self.assertAlmostEqual(get_area(14),615.75164)
    def test_perimeter(self):
        self.assertAlmostEqual(get_perimeter(6),37.699079999999995)
        self.assertAlmostEqual(get_perimeter(12),75.39815999999999)
        
unittest.main()

"""
MANTIQIY QIYMATLARNI TEKSHIRISH
Agar funksiya mantiqiy qiymat qaytarsa, bunday funksiyalarni assertTrue() va assertFalse() metodlari yordamida tekshirishimiz mumkin. 
Quyidagi funksiyamiz kiritilgan son tub yoki yo'q ekanini tekshiradi:
def tubSonmi(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
        if n%i==0:
            return False   
    return True
Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun tubSon_test.py dasturini yozamiz:
import unittest
from tubSonmi import tubSonmi
​
class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))
        
unittest.main()
Test davomida tubSonmi() funksiyasini bir nechta tub (7, 193, 547) va tub bo'lmagan (6, 265, 489) sonlar bilan chaqirdik. Bunda assertTrue() metodi funksiyamiz haqiqatdan ham True qiymatini qaytarishini, assertFalse() metodi esa funksiyamiz False qiymat qaytarishini tekshiradi.
TAQQOSLASH METODLARI
TestCase klassi tarkibidagi boshqa taqqoslash metodlari ham mavjud:
https://python.sariq.dev/testing/36-function-test
"""