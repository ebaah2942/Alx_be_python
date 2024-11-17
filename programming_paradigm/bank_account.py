class BankAccount:
    def __init__(self, current_balance=0):
    
        self.current_balance = current_balance


    def deposit(self, amount):
        self.current_balance += amount
        
    def withdraw(self, amount):
        if amount > self.current_balance:
            return False
        else:    
            self.current_balance -= amount
            return True

   
    def display_balance(self):
        print(f"Current Balance: ${self.current_balance:.2f}")


      

