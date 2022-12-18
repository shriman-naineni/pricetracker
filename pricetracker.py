import requests
from bs4 import BeautifulSoup

def price(soup):
    pprice = soup.find(id="tp_price_block_total_price_ww").find("span").text
    return pprice

def avail_check(soup):
    available = soup.find("div", attrs={'id':'availability'})
    available = available.find("span")
    return available.text.strip()

if __name__ == '__main__':
    link = "https://www.amazon.in/New-Apple-iPhone-12-64GB/dp/B08L5TGWD1/ref=sr_1_2?crid=ISGOFU233G7K"
    HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    print("Product Price =", price(soup))
    print("Availability =", avail_check(soup))


