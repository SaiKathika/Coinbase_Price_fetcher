from notify_run import Notify   #To get notification on Mobile
import requests
import json
import time
from win10toast import ToastNotifier    #To get notification on Windows 10

notify = Notify()

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
    
    #can change the Crypto and conversion price and price type [BTC or XRP etc]-[USD or INR etc]/[buy or sell or spot]
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/buy")
    #This line is used to display on terminal
    print(f"Buy_Price: {price.display()}")

    #This line is used to send notification to Mobile
    notify.send(f"Buy_Price: {price.display()}")     
    
    #This line is used to send notification to Windows 10 Screen
    toaster.show_toast(f"Buy_Price: {price.display()}")   

    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/sell")
    print(f"Sell_Price: {price.display()}")
    
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-INR/spot")
    print(f"Spot_Price: {price.display()}")

    #sleep function will trigger for every 2 Minutes
    time.sleep(120)
