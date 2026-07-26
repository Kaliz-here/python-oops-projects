class BankAccount:
    # init atributes
    # step 1
    def __init__(self, holder_name: str, account_number: str, balance: float):
        self.holder_name = holder_name
        # validation on account number
        if(len(account_number) < 15):
            raise ValueError("Account number must be 15 digits")

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

account_object_list = []
account_object_dict = {}
start = 0

# Conditions for actions
def actions():
    print("""
        1. Check Balance
        2. Transfer Money
        3. Account Details
        4. Exit session
    """)

while True:
    actions()
    account_name = input("Enter Name : ")
    account_number = input("Enter account number : ")
    account_balance = float(input("Enter Balance : "))

    # add account in list
    accounts = BankAccount(account_name, account_number, account_balance)
    account_object_list.append(accounts)


for i in account_object_list:
    print(i)