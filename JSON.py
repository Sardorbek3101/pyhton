# =============================================================================
# import json
# 
# x = 10
# x_json = json.dumps(x)
# #print(x_json)
# #print(type(x_json))
# 
# y = 5.5
# y_json = json.dumps(y)
# #print(y_json)
# 
# m = True
# m_json = json.dumps(m) 
# #print(m_json)
# #print(type(m_json))
# 
# # =============================================================================
# # ism = "Sardor"
# # ism_json = json.dumps(ism)
# # familiya_json = json.dumps("Olimjonov")
# # print(familiya_json)
# # 
# # =============================================================================
# 
# sonlar = (12 , 45 , 23 , 67)
# sonlar_json = json.dumps(sonlar)
# #print(sonlar_json)
# 
# bemor = {
#     'ism' : "Alijon Valiyev",
#     'yosh' : 30,
#     'oila' : True,
#     "farzndlar" : ("Ahmad" , "Bonu"),
#     "allergiya" : None,
#     "dorilar" : [
#         {'nomi' : 'analgin' , 'miqdori' : 0.5},
#         {'nomi' : 'Panadol' , 'miqdori' : 1.2},
#         ]
#     }
# bemor_json = json.dumps(bemor , indent = 4) #indent = 4 - bu har bir kod boshida 4 ta probeldan qo'shib ketish
# # =============================================================================
# # print(bemor_json)
# # =============================================================================
# 
# with open("bemor.json" , 'w') as f:
#     json.dump(bemor , f) #o'zgaruvchini json formatdagi faylga joylash
#     
# bemor2 = json.loads(bemor_json) #JSON formatidagi kodlarni python ga uzgartirip yuklab olish
# 
# with open("bemor.json") as f:
#     bemorr = json.load(f) #JSON formatidagi faylni python tiliga yuklab olish
# 
#     print(bemorr)
# =============================================================================
# =============================================================================
# import json
# import googlemaps
# from apikey import APICEY
# 
# ##GoogleMaps
# gmaps = googlemaps.Client(key=APICEY)
# 
# data = gmaps.geocode('Nurota , Navoiy , Uzbekistan')
# 
# g = json.dumps(data[0] , indent = 4 , sort_keys=True)
# print(g)
# =============================================================================
