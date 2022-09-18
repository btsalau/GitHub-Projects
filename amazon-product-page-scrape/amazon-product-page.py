import requests
from bs4 import BeautifulSoup
from pprint import pprint

baseurl = 'https://www.amazon.co.uk/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

url = requests.get('https://www.amazon.co.uk/Invision%C2%AE-Ultra-Swivel-Bracket-Mount/dp/B010G6972O/ref=sr_1_3?_encoding=UTF8&c=ts&dchild=1&keywords=TV+Mounts%2C+Stands+%26+Turntables',
                   headers=headers)
soup = BeautifulSoup(url.content, 'lxml')

# print(url.status_code)

name = soup.find('span', class_='a-size-large product-title-word-break').text.strip()

buy_now_price = soup.find('span', class_='a-offscreen').text

vendor = soup.find('a', id='sellerProfileTriggerId').text

# insurance = soup.find('a', id='mbbPopoverLink').text

insurance_two = soup.find_all('a', id='mbbPopoverLink')  # returns insurance list

product_details = soup.find('ul', class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')

product_details_breakdown = product_details.find_all('span', class_='a-list-item')[0]

print(f'''
{name}, 
{buy_now_price}, 
{vendor},
{product_details}, 
{product_details_breakdown}
''')

