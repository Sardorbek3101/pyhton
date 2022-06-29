class Car:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self , make , model , year , km = 0 , price = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km 
    
    def set_price(self , price):
        self.price = price
        
    def add_km(self , km):
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas") #raise uzimiz error yasaymiz
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.upper()} "
        info += f"{self.year} - yil , {self.__km}km yurgan" 
        if self.price:
            info += f"Narhi : {self.price}"
        return info
        
    def get_km(self):
        return self.__km