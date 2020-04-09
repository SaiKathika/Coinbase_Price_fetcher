import requests
import json
import time
from win10toast import ToastNotifier    #To get notification on Windows 10

toaster = ToastNotifier()

class Price:
    
    def display(self):
        data = response.json()
        #This line gets the Cryptocurrency name
        crypto = data["data"]["base"]
        #This line gets the Price
        price = data["data"]["amount"]
        return price

while True:
    print("Ethereum")
    price = Price()
    
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/buy")  
    
    #This line is used to send notification to Windows 10 Screen
    toaster.show_toast(f"Buy_Price: {price.display()}")   

    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/sell")
    #This line is used to send notification to Windows 10 Screen
    toaster.show_toast(f"Sell_Price: {price.display()}") 

    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/spot")
    #This line is used to send notification to Windows 10 Screen
    toaster.show_toast(f"Spot_Price: {price.display()}") 