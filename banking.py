"""
banking.py
"""
from datetime import datetime
from decimal import Decimal
class Account():
    """
    Account class
    """
    #transactions: list = field(default_factory=list)
    def __init__(self):
        self.transactions = []

    def get_balance(self):
        """
        get balance from transactions list
        """
        balance = 0
        balance = sum(transaction.amount for transaction in self.transactions)
        return balance

    def deposit(self,amount):
        """
        deposite amount
        """
        if amount < 0:
            amount = abs(amount)
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def withdraw(self,amount):
        """
        withdraw amount
        """
        if amount > 0:
            amount = -amount
        transaction = Transaction(amount)
        self.transactions.append(transaction)


class Transaction():
    """
    Transaction class
    """
    amount: Decimal
    timestamp: datetime

    def __init__(self,amount,timestamp = None):
        self.amount = amount
        if timestamp is None:
            self.timestamp = datetime.now().strftime("%Y, %m, %-d, %H, %M, %S")
        else:
            self.timestamp = timestamp

    def __str__(self):
        if self.amount > 0:
            string = f'{self.timestamp.date()}: +${self.amount:,.2f}'
        elif self.amount < 0:
            string =f'{self.timestamp.date()}: -${abs(self.amount):,.2f}'
        else:
            string =f'{self.timestamp.date()}: ${self.amount:,.2f}'
        return string

    def __repr__(self):
        return f"Transaction(amount='{self.amount}',timestamp='{self.timestamp}')"

    def __eq__(self, other):
        """Returns True if amount and timestamp are identical."""
        return self.amount == other.amount and self.timestamp == other.timestamp
