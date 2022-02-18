from turtle import width


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        deposit = int(input())
        return self.balance + deposit

    def withdraw(self):
        withdraw = int(input())
        if withdraw > self.balance:
            return 'balance is low'
        else:
            return self.balance - withdraw

P1 = Account('Akzhol', 25000)

print(P1.withdraw())