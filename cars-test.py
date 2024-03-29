import unittest
from cars import Car

class CarTest (unittest.TestCase):
    def setUp(self):
        make = 'GM'
        self.model = 'Malibu'
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make , self.model , year)
        self.avto2 = Car(make , self.model , year , price = self.price)
        
    def test_create(self):
        #Qiymat mavjutligini assertIsNotNone metodi bila tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertEqual(self.model, self.avto1.model)
        ##Qiymat mavjut emasligini assertIsNone metodi bila tekshirish
        self.assertIsNone(self.avto1.price)
        #Qiymat tengligini assertEqual bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        #avto2 ni narhini tekshiramiz
        self.assertEqual(self.price, self.avto2.price)
        
        def test_set_price(self):
            new_price = 450000
            self.avto2.set_price(new_price)
            self.assertEqual(new_price , self.avto2.price)
        
        def test_add_km(self):
            self.avto1.add_km(self.km)
            self.assertEqual(self.avto1.get_km(), self.km)
            self.avto1.add_km(5000)
            self.assertEqual(15000 , self.avto1.get_km())
            
            new_km = -5000
            try:
                self.avto1.add_km(new_km)
            except ValueError as error:
                self.assertEqual(type(error) , ValueError)
                
unittest.main()