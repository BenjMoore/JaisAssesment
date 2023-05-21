
import time
from libs.version import *
from twilio.rest import Client
import random
import os
from twilio.rest import Client
import sqlite3
account_sid = 'ACfceec9936329f15857f4679e3fa75880'
auth_token = '63c195cdcbf7b0f1e13d1764bcd4061c'

con = sqlite3.connect("tutorial.db")
RandomQuote = "random.choice()"
# Download the helper library from https://www.twilio.com/docs/python/install

Quotes = []

##

def main():

    number = []

    Number1 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    if Number1 == "Done":
        number.insert(1,[Number1])
    
    Number2 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    if Number2 == "Done":
        number.insert(2,[Number2])
    
    Number3 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    if Number3 == "Done":
        number.insert(3,[Number3])
    
    Number4 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    if Number4 == "Done":
        number.insert(4,[Number4])
    
    Number5 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    if Number5 == "Done":
        number.insert(5,[Number5])
    
    

    
    

    if NumberIterator == "Done":
        print("Sending... Please wait!")
        number1 = number[0][0]
        number2 = number[1][0]
        number3 = number[2][0]
        number4 = number[3][0]
        number5 = number[4][0]
        numbers = [number1]
        
    pass



def sendMsg1(numbers):
    client = Client(account_sid, auth_token)
        
    message = client.messages.create(
    body=f"{RandomQuote}",
    from_="+12543182841",
    to=f"{numbers[i]}"
)
    time.sleep(10)
    i = i + 1
    pass




if __name__ == "__main__":
    main()
