
from os import error
import random
import time
from libs.version import *
from twilio.rest import Client
import sqlite3

account_sid = 'ACfceec9936329f15857f4679e3fa75880'
auth_token = '5a4a508d1c5a37c91e8e81b0f42b724b'


# Download the helper library from https://www.twilio.com/docs/python/install

Quotes = []

##

def main():

    conn = sqlite3.connect('InspirationalQuotes.db')

    cursor = conn.execute("SELECT Quote from QUOTES")
    
    i = 0
    for row in cursor:
         quote = row[0]
         Quotes.insert(i,quote)
         print(quote)
         i = i + 1

       
    Number1 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    
    
    Number2 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    
    
    Number3 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    
    
    Number4 = input(">> Enter Phone Number (Include Area Code [+61]) ")
   
    
    Number5 = input(">> Enter Phone Number (Include Area Code [+61]) ")
    
   
    print("Sending... Please wait!")

    numbers = []
    numbers.insert(1,Number1)
    numbers.insert(2,Number2)
    numbers.insert(3,Number3)
    numbers.insert(4,Number4)
    numbers.insert(5,Number5)


    client = Client(account_sid, auth_token)
    Count = len(numbers)

    i = 0

    RandomQuote = random.choice(Quotes)

    for i in range(Count):
        if numbers[i] == '0':
            i = i + 1
            pass

        else:
            message = client.messages.create(

            body=f"{RandomQuote}",
            from_="+12543182841",
            to=f"{numbers[i]}"
                                            )
            time.sleep(5)
            print(numbers[i])
            i = i + 1
    pass




    
if __name__ == "__main__":
    main()
