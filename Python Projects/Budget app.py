import re

class Category:
    def __init__(self, name):
        self.name = name 
        self.ledger = list()

    def deposit(amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(amount, description=""):
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance():
        balance = 0
        for transaction in self.ledger:
            splitted = re.split(", ", transaction)
            for chunk in splitted:
                if type(chunk) == int or type(chunk) == float:
                    balance += chunk


food = Category("Food")
food.deposit(1000)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())



                
