
import sys
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['fname']
        processed_text = text.upper()

        print(processed_text)
        return processed_text


if __name__ == "__main__":
    app.run()

import requests
response=requests.get("https://api.documenu.com/v2/restaurants/zip_code/30047?key=7c661110cc638d88e9950b709dc1b4e3")
data=response.json()
for x in data["data"]:
    if x["restaurant_name"] == '':
        name = "none available" 
    else:
        name = x["restaurant_name"]
        
    if x["restaurant_phone"] == '':
        phone = "none available"
    else:
        phone = x["restaurant_phone"]


    if x["restaurant_website"] == '':
        website = "none available"
    else:
        website = x["restaurant_website"]


    if x["price_range"] == '':
        price = "none available"
    else:
        price = x["price_range"]


    if x["hours"] == '':
        hours = "none available"
    else:
        hours = x["hours"]


    print("The name of the restaurant is " + name + " , and here is their information:")
    print("Phone number: " + phone)
    print("Their website can be found: " + website)
    print("Their price range is: " + price)
    print("Their hours are: " + hours)

    if x["cuisines"] == [""]:
        cuisines = "none available"
        print("Their cuisines are listed as: " + cuisines)
    else:
        print("Their cuisines are listed as: ")
        for food in x["cuisines"]:
            print(food)
            
    
    

    
    
