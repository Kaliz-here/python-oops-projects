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