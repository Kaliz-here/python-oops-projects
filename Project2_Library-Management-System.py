class LibrarySystem:
    def __init__(self, title, author, isbn, available=True, borrower_name=None):
        if(title == "" or author == ""):
            raise ValueError("input cannot be empty..!")
        else:
            self.title = title
            self.author = author

        if(len(isbn) != 6):
            raise ValueError("Invalid ISBN NO.")
        else:
            self.isbn = isbn

        self.available = available
        self.borrower_name = borrower_name

    # Book borrow method
    def borrow_book(self, borrower_name):
        pass

    def return_book(self):
        pass

    # object ouput method
    def __str__(self):
        details = f"\Title: {self.title}\n"
        details += f"Author : {self.author}\n"
        details += f"ISBN : {self.isbn}\n"
        details += f"Status : {self.available}"

        return details
        

book_list = []
book_dict = {}

books_count = int(input("\nHow many books add in library : "))

start = 1
while start <= books_count:
    title = input("Enter Title : ")
    author = input("Enter Author : ")
    isbn = input("Enter ISBN : ")

    # add book in list
    book = LibrarySystem(title, author, isbn, available=True, borrower_name=None)
    book_list.append(book)

    # add book in dict search using isbn
    book_dict[isbn] = book

    start += 1

def employee_menu():
    while True:
        print("""
                1. Search Book
                2. Add Book
                3. Remove Book
                4. Print All Book
                5. Total Books
                6. Available Books
                7. Exit""")

def customer_menu():
    while True:
        print("""
                1. Borrow Book
                2. Return Book
                3. Search Book
                4. View Available Book
                5. Exit
                """)


print("\n1. Employee Menu")
print("2. Customer Menu")
userchoice = int(input("\nEnter your choice : "))

if(userchoice == 1):
    employee_menu()

elif(userchoice == 2):
    customer_menu()

else:
    print("Invalid userchoice..!")
