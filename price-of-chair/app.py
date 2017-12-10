__author__='miumiu'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip() # "£129.00"

price_without_symbol = string_price[1:]
price = float(price_without_symbol)
if(price < 200):
    print("buy the chair")
    print("the current price is {}.".format(string_price))
else:
    print("don't buy it")


#<span itemprop="price" class="now-price">£129.00</span>


