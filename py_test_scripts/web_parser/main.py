from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests
import smtplib


# SMTP connection
my_email = "{EMAIL}"
my_pass = "{PASSWORD}"
# noinspection SpellCheckingInspection
connection = smtplib.SMTP("{SMTP_SERVER}")
connection.starttls()
connection.login(user=my_email, password=my_pass)

msg = EmailMessage()
msg['Subject'] = "{SUBJECT}"
msg['From'] = my_email
msg['To'] = "{DESTINATION_EMAIL}"

web_url = "https://hotline.ua/bt-roboty-pylesosy/irobot-roomba-i3/?tab=prices&filter=official"
# noinspection SpellCheckingInspection
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

lover_price = 11999

for shop in shops_list:
    shop_name = shop.find(name="a", class_="shop__title mb-row").getText()
    current_price = shop.find(name="span", class_="price__value").getText()

    int_current_price = int("".join(current_price.split()))

    if lover_price > int_current_price:
        lover_price = int_current_price
        message = shop_name.strip() + "=" + current_price
    else:
        message = "Price didn't change(("

    msg.set_content(message)

connection.send_message(msg)
connection.quit()
