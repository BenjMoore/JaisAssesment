
from os import error
import time
from libs.version import *
from twilio.rest import Client
import sqlite3
account_sid = 'ACfceec9936329f15857f4679e3fa75880'
auth_token = '63c195cdcbf7b0f1e13d1764bcd4061c'

con = sqlite3.connect("InspirationalQuotes.db")
RandomQuote = "random.choice()"
# Download the helper library from https://www.twilio.com/docs/python/install

Quotes = []

##

def main():

    create_connection('InspirationalQuotes.db')

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
            time.sleep(10)
            print(numbers[i])
            i = i + 1
    pass



def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except error as e:
        print(e)

    return conn


def select_all_quotes(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)
if __name__ == "__main__":
    main()
