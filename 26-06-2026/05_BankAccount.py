class BankAccount:
    Bank_name = "Bank Of India\n"

    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance


    def Deposite(self, amount):
        self._balance += amount
        print(f"Fund Added : {amount}")

    def withdraw(self, amount):
        if(self._balance >= amount):
            self._balance -= amount
            print(f"Withdraw Amount : {amount}")
        else:
            print("Insufficient Balance")

    def showBalance(self):
        print(f"Balance : {self._balance}\n")

user_1 = BankAccount("Manav Kamble", 0.0)

print(user_1.Bank_name)
user_1.showBalance()

user_1.Deposite(1000)
user_1.showBalance()

user_1.Deposite(200)
user_1.showBalance()

user_1.withdraw(100)
user_1.showBalance()

# user_1.withdraw(10000)
# user_1.showBalance()

user_1.withdraw(1000)
user_1.showBalance()