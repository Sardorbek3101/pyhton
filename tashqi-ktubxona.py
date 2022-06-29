#GOOGLE TRANSLATOR
# =============================================================================
# #pip install googletrans==3.1.0a0
# from googletrans import Translator
# 
# msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun \"q\" deb yozing)"
# tarjimon = Translator()
# while True:
#     text = input(msg)
#     if text == 'q':
#         break
#     else: 
#         tarjima = tarjimon.translate(text , srs='uz' , dest = 'en')
#         print(tarjima.text)
# =============================================================================
#requests
# =============================================================================
# #pip install requests
# import requests
# from pprint import pprint
# 
# # =============================================================================
# # sahifa = 'https://kun.uz/'
# # r = requests.get(sahifa)
# # pprint(r.text)
# # =============================================================================
#     
# # restcountries API
# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json.keys())
# print(r_json['capital'])
# 
# =============================================================================
# =============================================================================
# import requests
# import googletrans
# 
# url = 'https://api.adviceslip.com/advice'
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)
# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest = 'uz')
# print(tarjima.text)
# =============================================================================
#BeautifulSoup
# =============================================================================
# import requests
# from pprint import pprint 
# from bs4 import BeautifulSoup
# 
# sahifa = 'https://kun.uz/news/main'
# r = requests.get(sahifa)
# #pprint(r.text)
# soup = BeautifulSoup(r.text , 'html.parser') #r ni textini htmlni qaytar
# #print(soup.prettify())
# news = soup.find_all(class_="news-title") #soup ni html dagi hamma "news-title" ismli classlarni qaytar
# print(news[0].text)
# =============================================================================
#pip install fuzzywuzzy
# =============================================================================
#fuzzywuzzy
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from uzwords import words
# # =============================================================================
# # #ikki so'z orasida o'xshashlik foizini topish
# # print(fuzz.ratio('salom' , 'assalom'))
# # print(fuzz.ratio('salom' , 'salim'))
# # =============================================================================
# 
# # =============================================================================
# # #Matnlar orasida 3 ta eng o'xshashlarini ajratib olish
# # text = 'салом'
# # matches = process.extract(text, words , limit = 3)
# # print(matches)
# # =============================================================================
# #Matnlar orasida eng o'xshashini ajratib olish
# text = 'антаркика'
# match = process.extractOne(text, words)
# print(match)
# =============================================================================
# =============================================================================
# import wx #wxPython 
# import wordcloud import WordCloud
# import sv2
# =============================================================================
