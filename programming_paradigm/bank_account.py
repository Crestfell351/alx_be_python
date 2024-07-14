class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0\
        
    def deposit(self,amount):
        self.account_balance += amount

    def withdraw(self,amount):
        if amount>0:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self,amount):
        print(f"Current Balance: ${amount}")
        
