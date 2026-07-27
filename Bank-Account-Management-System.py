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

account = int(input("How many account -> "))
start = 1

while(start <= account):

    print(f"\n\nAccount --> {start}")

    account_name = input("\nEnter Name -> ")
    account_number = input("Enter account number -> ")
    account_balance = float(input("Enter Balance -> "))

    # add account in list
    accounts = BankAccount(account_name, account_number, account_balance)
    account_object_list.append(accounts)

    # add account in dict
    account_object_dict[account_number] = accounts

    start += 1 #how many account add in list and dict

# Function for employee
def employee():
    while True:
        print("""
                1. Search Account Holder (Administrator Only)
                2. Richest Account (Administrator Only)
                3. Poorest Account (Administrator Only)
                4. Print All Accounts (Administrator Only)
                5. Exit
        """)

        user_choice = int(input("\nEnter Your Choice -> "))

        # Search Account Holder
        if user_choice == 1:
            ac_number = input("Enter account number -> ")
            if(ac_number in account_object_dict):
                print(account_object_dict[ac_number])
        
            else:
                print("Account Not Found..!")

        # Richest Account
        elif(user_choice == 2):
            richest_temp = account_object_list[0]
            for richest in account_object_list:
                if(richest.balance > richest_temp.balance):
                    richest_temp = richest
            print(" | Richest Account |")
            print(richest_temp)

        # Poorest Account
        elif(user_choice == 3):
            poorest_temp = account_object_list[0]
            for poorest in account_object_list:
                if(poorest.balance < poorest_temp.balance):
                    poorest_temp = poorest
            print(" | Poorest Account |")
            print(poorest_temp)

        # Print All Accounts
        elif(user_choice == 4):
            for all_accounts in account_object_list:
                print(all_accounts)

        # break loop
        elif(user_choice == 5):
            break

# Function for Customer
def custormer():
    while True:
        print("""
                    1. Deposit Money
                    2. Withdraw Money
                    3. Transfer Money
                    4. Exit
            """)

        user_choice = int(input("\nEnter Your Choice -> "))

        if (user_choice == 1):
            pass

        elif(user_choice == 2):
                    pass
        
        elif(user_choice == 3):
            pass
        
        elif(user_choice == 4):
            break


        
# Get verification from user
print("\n\nC - Customer | E - Employee")
verification = input("\nAre you customer or employee -> ")

if verification == "E" or verification == "e":
    employee()
elif verification == "C" or verification == "c":
    custormer()
else:
    print("Enter Valid Input")