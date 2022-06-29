# =============================================================================
# #Object oriented
# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def get_name(self):
#         return self.name
#     def get_lastname(self):
#         return self.familiya
#     def get_age(self , yil):
#         return yil - self.tyil
#     def tanishtir(self):
#         return f"Mening ismim {self.ism} {self.familiya}, tugulgan yilim {self.tyil} yil"
# talaba1 = Talaba('Sardorbek', 'Olimjonov', 2006)
# talaba2 = Talaba('Hasan','Husanov', 2000)
# talaba3 = Talaba('Alibek', 'Valibekov', 2004)
# print(talaba1.ism)
# print(talaba1.tanishtir())
# print(talaba3.get_lastname())
# print(talaba2.get_age(2022))
# =============================================================================

# =============================================================================
# #VORISLIK
# 
# class Shaxs:
#     """Shaxslar haqida malumot"""
#     def __init__(self , ism , familiya , passport , tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#     def get_info (self):
#         """shaxs haqida malumot"""
#         info = f"{self.ism} {self.familiya}, "
#         info += f"pasport: {self.passport}, {self.tyil} yil da tugulgan"
#         return info
#     def get_age(self, yil):
#         """shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
# 
# inson = Shaxs('Sardorbek', 'Olimjonov', 'S20063101', 2006)
# print(inson.get_age(2022))
# 
# 
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, passport, tyil, idraqam , manzil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#     def get_id(self):
#         """Talabaning id raqami"""
#         return self.idraqam
#     def get_bosqich(self):
#         """talbaning bosqichi"""
#         return self.bosqich
#     #POLIMORFIZM
#     def get_info (self):
#         """shaxs haqida malumot"""
#         info = f"{self.ism} {self.familiya}, "
#         info += f"{self.bosqich} - bosqich, ID raqami: N00001"
#         return info
# 
# class Manzil:
#     """Manzilni saqlash uchun klass"""
#     def __init__(self , uy , kocha , tuman , viloyat):
#         """Manzil xusussiatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#     
#     def get_manzil(self):
#         """Manzilni korish"""
#         manzil = f"{self.viloyat} viloyati , {self.tuman} tumani, "
#         manzil  += f"{self.kocha} kochasi , {self.uy} - chi uy"
#         return manzil
# 
# talaba1_manzil = Manzil(50, 'Shodlik', 'Nurota', 'Navoiy')
# talaba1 = Talaba('Olimjonov', 'Sardorbek', 'S20063101', 2006, 'S3101', talaba1_manzil)
# print(talaba1.get_info())
# print(talaba1.manzil.get_manzil())
# # =============================================================================
# # talaba1 = Talaba('Sardorbek', 'Olimjonov', 'S20063101', 2006, 'S3101')
# # print(talaba1.get_info())
# # print(talaba1.get_id())
# # =============================================================================
# =============================================================================

# =============================================================================
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self , make , model , rang , yil , narh , km = 1000):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km #INKAPSULIATSIYA
#         self.__id = uuid4() 
#         Avto.__num_avto += 1
#         
#     @classmethod
#     def get_num_avo(cls):
#         return cls.__num_avto
#     
#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
#     def add_km(self , km):
#         if km >= 0:
#             self.__km += km
#         else:
#             return "Mashina km kamaytirib bo'lmaydi"
#     
# avto1 = Avto('Gm', 'Malibu', 'Qora', 2020, 40000 , 1000)
# avto2 = Avto('Gm', 'Malibu', 'Qora', 2020, 40000 , 1000)
# avto3 = Avto('Gm', 'Malibu', 'Qora', 2020, 40000 , 1000)
# print(avto1.get_id())
# avto1.add_km(2000)
# print(avto1.get_km())
# print(Avto.get_num_avo())
# print(avto1.get_num_avo())
# =============================================================================
#DUNDER METODLaR
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self , make , model , rang , yil , narh , km = 1000):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
        
# =============================================================================
#     def __str__(self):
#         return f"Avto: {self.make} {self.model}" 
# =============================================================================
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.narh == y.narh
    def __lt__(self , y):
        return self.narh < y.narh
    def __le__(self , y):
        return self.narh <= y.narh
    
class AvtoSalon:
    def __init__(self , name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self , index , qiymat):
        self.avtolar[index] = qiymat
        
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        return [avto for avto in self.avtolar]
    
    def __add__(self , y):
        if isinstance(y, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            self.add_avto(y)
            
    def add_avto(self , *qiymat):
        for avto in qiymat:
            if isinstance(avto , Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiritng")

salon1 = AvtoSalon("MaxAvto")
avto1 = Avto('Gm', 'Malibu', 'Qora', 2020, 40000 , 1000)
avto2 = Avto('Gm', 'Lacetti', 'Oq', 2018, 20000 , 1000)
avto3 = Avto('Toyota', 'Carolla', 'Silver', 2018, 450000)
avto4 = Avto('Mazda', 6, 'Qizil', 2015, 35000)
avto5 = Avto('Volkswagen', 'Polo', 'Qora', 2015, 300000)
avto6 = Avto('Honda', 'Accord', 'Oq', 2017, 420000)

# =============================================================================
# salon1.add_avto(avto1 , avto2 , avto3)
# 
# salon1[1] = Avto('lamorgini' , 'urus' , 'sariq' , 2020 , 500000)
# =============================================================================
# =============================================================================
# print(avto1)
# print(repr(avto1))  
#       
# print(avto1 == avto2)
# print(avto1 < avto2)
# print(avto1 >= avto2)
# =============================================================================

# =============================================================================
# print(salon1[1])
# print(salon1[:])
# ============================================================================

salon1(avto1 , avto2 , avto3)

salon2 = AvtoSalon("Avto Lider")
salon2(avto4 , avto5 , avto6)

salon3 = salon1 + salon2
salon1 + avto4
print(salon1())
print(salon3)
print(salon3())

get_info