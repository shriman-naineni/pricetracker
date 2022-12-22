import requests
from bs4 import BeautifulSoup

user = input("what item would you like to search for: ")
search = user.replace(" ","+")

link = f"https://www.flipkart.com/search?q={search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
print(link)
HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
webpage = requests.get(link, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

price = soup.find("div", class_ = "_30jeq3 _16Jk6d").text
avail = soup.find("div", class_ = "_1dVbu9")
print("Product Price =", price)
if avail == None:
    print("Availability = In stock.")
else:
    print("Availability =", avail.text)