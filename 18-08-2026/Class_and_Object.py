class bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("insufficient balance")
    def display(self):
        print("name:", self.name)
        print("balance:", self.balance)
account = bank("sherif", 5000)
account.deposit(2000)
account.withdraw(1000)
account.display()
