class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.accounts = []

    def make_deposit(self, amount):
        self.account.deposit(amount)
        
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)

        return self

    def display_account_info(self):
        self.account.display_account_info()

        return self

# *************************************************************************


class BankAccount:		
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        print(f"Deposting {amount}")
        self.balance += amount

        return self

    def withdraw(self, amount):
        if(self.balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:    
            print(f"Withrawing {amount}")
            self.balance -= amount

        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)

        return self    


hyunsoo = User('Hyunsoo', 'hanson@gmail.com')

hyunsoo.account.display_account_info()
hyunsoo.make_deposit(900)
hyunsoo.account.display_account_info()
hyunsoo.make_withdraw(250)
hyunsoo.account.display_account_info()

