#Umkc-Directory listing its prices for every course
price_book={"python-Deep Learning" : "20", "web Design" : "25",
            "machine-Learning" : "40", "network-Architecture" : "50"}
print(price_book)

#For the Range from start to end
x=int(input("Enter the starting number"))

y=int(input("Enter the final number"))
#Passing every book and its price
for book,cost in price_book.items():
    if int(cost) in range(x,y+1):
        print('%s: %s' %(book,cost))