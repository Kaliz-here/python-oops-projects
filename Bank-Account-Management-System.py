class BankAccount:
    # init atributes
    # step 1
    def __init__(self, holder_name: str, account_number: str, balance: float):
        self.holder_name = holder_name
        # validation on account number
        if(len(account_number) < 15):
            raise ValueError("Account number must be 10 digits")

        else:
            self.account_number = account_number

        #validation on user balance
        if(balance >= 0):
            self.balance = balance
        else:
            raise ValueError("Balance must be positive value")

    # Add deposite method
    def deposite(self, amount):
        self.balance += amount
        print(f"Fund Added : {amount}")

    # Add Withdraw method
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdraw {amount}")
