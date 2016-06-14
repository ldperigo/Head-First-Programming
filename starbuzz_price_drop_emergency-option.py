import urllib.request
import time
from time import strftime

#This is the start of the function
def get_price():
    #Open the page and read to a buffer
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    #Read the page to a string
    text = page.read().decode("utf8")
    #Find the ">$" from the source code page/string; using a regular expression here would be better
    where = text.find('>$')
    start_price = where + 2
    end_price = start_price + 4
    return float(text[start_price:end_price])
#This is the end of the function

price_now = input("Do you need a price immediately? ")
if price_now == "y":
    print("Emergency Price is ", get_price())
    print("Price retrieved on ", strftime("%Y-%m-%d:%H:%M"))

else:
    price = 99.99
    while price > 4.74:
        time.sleep(5)
        price = get_price()
    print("Buy Now, because the price is low ", get_price())
    print("Price retrieved on ", strftime("%Y-%m-%d:%H:%M"))
    
        
        
    

