class BankAccount:
    # init atributes
    # step 1
    def __init__(self, holder_name: str, account_number: str, balance: float):
        self.holder_name = holder_name
        # validation on account number
        if(len(account_number) < 15):
            raise ValueError(f"Account number must be 15 digits | You enterd ({len(account_number)}) numbers")

        else:
            self.account_number = account_number

        #validation on user balance
        if(balance >= 0):
            self.balance = balance
        else:
            raise ValueError("Balance must be positive value")

    # Add deposite method
    def deposit(self, amount):
        if(amount <= 0):
            raise ValueError("Invalid deposit money")
        else:
            self.balance += amount
            print(f"Available Balance : {self.balance}")


    # Add Withdraw method
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"Withdraw Amount : {amount}")
        else:
            raise ValueError("Insufficient Balance")

    # Add transfer fund method
    def transfer(self, account_holder, account_number, amount):
        pass

    # Add __str__ method
    def __str__(self):
        details = f"\nName: {self.holder_name}\n"
        details += f"Account Number : {self.account_number}\n"
        details += f"Balance : {self.balance}"
        return details

account_object_list = [] # list of account holders
account_object_dict = {} # dict of account holder

account = int(input("How many account : "))
start = 0

while(start < account):

    print(f"Account --> {start}")

    account_name = input("\nEnter Name : ")
    account_number = input("Enter account number : ")
    account_balance = float(input("Enter Balance : "))

    # add account in list
    accounts = BankAccount(account_name, account_number, account_balance)
    account_object_list.append(accounts)

    start += 1 #how many account add in list and dict

# for i in account_object_list:
#     print(i)