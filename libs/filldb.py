import sqlite3


conn = sqlite3.connect('InspirationalQuotes.db')
cursor = conn.execute("SELECT * from QUOTES")

daQuotes = [
                "..my music isn't just music- its medicine",
                "Believe in your flyness...conquer your shyness",
                "Society has put up so many boundaries, so many limitations on what’s right and wrong that it’s almost impossible to get a pure thought out. It’s like a little kid, a little boy, looking at colors, and no one told him what colors are good, before somebody tells you you shouldn’t like pink because that’s for girls, or you’d instantly become a gay two-year-old. Why would anyone pick blue over pink? Pink is obviously a better color. Everyone’s born confident, and everything’s taken away from you",
                "I am not a fan of books. I would never want a book's autograph.",
                "'ll say things that are serious and put them in a joke form so people can enjoy them. We laugh to keep from crying."]
x = 0
for x in range(len(daQuotes)):
    conn.execute(f"INSERT INTO QUOTES(ID,Quote,QUOTES_STR) \
    VALUES ({x}, '{daQuotes[x]}', '{x}' )");
    x = x + 1