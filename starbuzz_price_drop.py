import urllib.request
import time

print("Let me know when coffee is below $4.74.")

price = 99.99
while price > 4.74:
    time.sleep(5)
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")

    where = text.find('>$')
    start_price = where + 2
    end_price = start_price + 4

    price = float(text[start_price:end_price])

print("Buy now, because it is at a low price!")
