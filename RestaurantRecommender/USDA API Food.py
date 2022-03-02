##import requests
##baseurl = "https://v2.jokeapi.dev/"
##fullurl = baseurl + "joke/Any?contains=computer"
##response = requests.get(fullurl) # requested the response
##data = response.json()
##
##for key in data.keys():
##    if key == "setup":
##        print (data[key])
##
##    if key =="delivery":
##        print (data[key])
##
##

import requests
baseurl = "https://api.documenu.com/v2/"
fullurl = baseurl + "restaurant/4072702673999819?key=0c1282aa00404ecfa47af6978f10de80"

response = requests.get(fullurl) # requested the response
data = response.json()

for dictionary in data.keys():
    newdict = data[dictionary]
    for subdict in newdict.keys():
        if subdict == "restaurant_name":
            print("The restuarant name you are looking for is " + newdict[subdict] + "!")

        if subdict == "restaurant_phone":
            print(newdict[subdict])

        if subdict == "restaurant_website":
            print(newdict[subdict])

        if subdict == "hours":
            print(newdict[subdict])

        if subdict == "price_range":
            print(newdict[subdict])

        if subdict == "cuisines":
            print(newdict[subdict])

        if subdict == "address":
            print(newdict[subdict])

