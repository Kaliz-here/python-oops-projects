class Book:
    def __init__(self, title, author, price):
        if price <= 0:
            raise ValueError("Invalid Price")
        
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"price : {self.price}\n")

    def apply_discount(self, percent):
        if(percent < 0 or percent >= 100):
            raise ValueError("Invalid Input")
        discount = self.price * percent / 100
        self.price = self.price - discount


book_1 = Book("python", "Manav", 550)
book_1.display()
book_1.apply_discount(10)
book_1.display()