class LibrarySystem:
    def __init__(self, title, author, isbn, available=True, borrower_name=None):
        if(title == "" or author == ""):
            raise ValueError("input cannot be empty..!")
        else:
            self.title = title
            self.author = author

        if(len(isbn) == 6):
            raise ValueError("Invalid ISBN NO.")
        else:
            self.isbn = isbn

    # Book borrow method
    def borrow_book(borrowr_name):
        pass

    def return_book():
        pass

    def __str__(self):
        pass