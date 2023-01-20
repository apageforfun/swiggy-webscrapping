from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

swiggy_url = requests.get("https://www.swiggy.com/city/mumbai/borivali-restaurants").text
swiggy_soup = BeautifulSoup(swiggy_url, "lxml")

items = swiggy_soup.find_all('div', class_='_3FR5S') #get all items on list

def restaurants():
    for index,item in enumerate(items):
        #For restaurants
        restaurant_name = item.find('div', class_='_3Ztcd').div.text
        timing = item.find_all('div', attrs={"class": None})[1].text
        discount = item.find('span', class_='sNAfh').text[0:3]
        ratings = item.find('div', class_='_3Mn31').div.text

        #For Items(Name, Price, Ratings)
        item_name = item.find('div', class_='_1gURR').text
        item_price = item.find('div', class_='nVWSi').text[0:4]


        
        print(f"Restaurant Details no.{index}:")
        print(f"Restaurant Name: {restaurant_name}")
        print(f"Discount avaliable: {discount}")
        print(f"Approximate delivery time: {timing}")
        print(f"Rating: {ratings}")
        print()
        print(f"Item details no.{index}:")
        print(f"Name of items available:{item_name}")
        print(f"Price:{item_price}")
        print()
        print()
        print()


restaurants()

