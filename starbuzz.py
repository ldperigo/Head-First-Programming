import urllib.request

print("What is the current price of coffee?")

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")

where = text.find('>$')

start_price = where + 2
end_price = start_price + 4

price = text[start_price:end_price]

print(price)
