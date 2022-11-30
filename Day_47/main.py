import requests
from bs4 import BeautifulSoup
import lxml

product_url = "https://www.amazon.com/MSI-GL66-Gaming-Laptop-i7-11800H/dp/B09127DDVT/ref=sr_1_3?crid=3RKNLV4DHA5DP&keywords=notebook+gamer&qid=1658849857&sprefix=notebook+gamer%2Caps%2C193&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(url=product_url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
response.raise_for_status()

with open("Day_47/product.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

product_price_span = soup.find(class_="a-price-whole")
product_price = product_price_span.get_text()
product_price = product_price.split(",")
product_price[1] = product_price[1][:3]
product_price = product_price[0] + product_price[1]
print(float(product_price))

# Use smtp to send a mail if price is below some preset value like $400