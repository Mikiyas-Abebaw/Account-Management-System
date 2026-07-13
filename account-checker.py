class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner                    
        self.account_number = account_number   
        self.__balance = balance                

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"--> Deposit Failed: Amount must be greater than 0 ETB.")
        else:
            self.__balance += amount
            print(f"--> Successfully deposited {amount} ETB.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"--> Withdrawal Failed: Amount must be greater than 0 ETB.")
        elif amount > self.__balance:
            print(f"--> Withdrawal Failed: Insufficient funds! Overdraft rejected.")
        else:
            self.__balance -= amount
            print(f"--> Successfully withdrew {amount} ETB.")

    def statement(self):
        """Prints a summary of the account status."""
        print(f"Account Statement:")
        print(f"  Owner:          {self.owner}")
        print(f"  Account Number: {self.account_number}")
        print(f"  Balance:        {self.__balance} ETB")
        print("-" * 35)



if __name__ == "__main__":
    
    # Create an account for Dawit with an initial balance of 1000 ETB
    acc = Account("Dawit", "100012345678", 1000)
    
    # 1. Check initial statement
    acc.statement()
    
    # 2. Test valid deposit
    acc.deposit(500)
    acc.statement()  
    
    # 3. Test invalid deposit (non-positive amount)
    acc.deposit(-50)
    
    # 4. Test valid withdrawal
    acc.withdraw(300)
    acc.statement()  
    
    # 5. Test invalid withdrawal 
    acc.withdraw(2000)  
    
   