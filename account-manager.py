class Account:
    def __init__(self, owner, bal):
        self.owner = owner
        self.balance = bal
    def deposit(self, amount):
        self.balance += amount
        return (owner,bal)
a = Account("Almaz", 1500)
a.deposit(500)
