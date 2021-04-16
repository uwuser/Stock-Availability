import requests
import time
from playsound import playsound
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
def send_notification():
    while True:
	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)
	print("In Stock PS5")
        playsound('alarm.mp3')


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("img", {"class": "oos-overlay hide"})
    return len(out_of_stock_divs) != 0


def check_inventory():
    url = "https://www.costco.ca/playstation-5-console-bundle.product.100696941.html"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        send_notification()
    else:
        print("PS5 Out of stock still")

while True:
    check_inventory()
    time.sleep(5)  # Wait a minute and try again

