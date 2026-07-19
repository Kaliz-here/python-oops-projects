# Library Management System

class Book:
    def __init__(self, title, author, price):
        self.title = title 
        self.author = author
        if price <= 0:
            raise ValueError("Invalid price...!")
        else:
            self.price = price

    #Calculate Discount Price
    def discount(self, dis):
        if dis >= 100 or dis < 0:
            raise ValueError("Invalid Discount..!")    
        else:
            discount_price = self.price * dis / 100
            final_price = self.price - discount_price
            self.price = final_price
            return self.price

    def __str__(self):
        return f"\nTitle : {self.title} | Author : {self.author} | Price : {round(self.price, 2)}"

books= []
library = {}
book_count = int(input("How many books : "))

for _ in range(1, book_count + 1):
    title = input("\nEnter Book Title : ")
    author = input("Enter Author : ")
    price = int(input("Enter Book Price : "))

    book = Book(title, author, price)
    books.append(book)
    library[title] = book

most_expensive = books[0]
cheapest = books[0]

for current_book in books:
    if(current_book.price > most_expensive.price):
        most_expensive = current_book

for current_book in books:
    if(current_book.price < cheapest.price):
        cheapest = current_book

print("\t\tExpensive Book : ", most_expensive)
print("\n\t\tCheapest Book : ", cheapest)

search_title = input("Enter Book Title : ")

if search_title in library:
    print(f"\nBook Found >> {library[search_title]}")

else:
    print("Book Not Found..!")