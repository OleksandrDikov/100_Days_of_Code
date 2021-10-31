from bs4 import BeautifulSoup
import requests


web_url = "https://hotline.ua/bt-roboty-pylesosy/irobot-roomba-i3/?tab=prices&filter=official"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                  ' Version/15.0 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Connection': 'keep-alive'
}
response = requests.get(web_url, headers=headers)
hotline_prices = response.text

soup = BeautifulSoup(hotline_prices, "html.parser")

all_shops = soup.find_all(name="div", class_="list")[1]
shops_list = all_shops.find_all(name="div", class_="list__item row flex")

for shop in shops_list:
    shop_name = shop.find(name="a", class_="shop__title mb-row").getText()
    current_price = shop.find(name="span", class_="price__value").getText()
    print(f"{shop_name.strip()} = {current_price}")
