"""
test_banking.py
"""
from datetime import datetime
from banking import Account
from banking import Transaction


def test_transaction_binds_amount_to_self():
    """
    test confirms the amount parameter is bound to self.
    """
    #这个不知道怎么写
def test_transaction_object_defaults_its_datetime_to_now():
    """
    The default timestamp should be now
    """
    transaction = Transaction(100)
    assert transaction.timestamp == datetime.now().strftime("%Y, %m, %d, %H, %M, %S")

def test_transaction_binds_timestamp_argument():
    """
    Test confirms the time parameter is bound to object
    """
def test_repr():
    """
    Test tests the result of __repr__ method
    """
    transaction =Transaction(amount='100',timestamp='datetime(2020, 10, 27)')
    expected = "Transaction(amount='100',timestamp='datetime(2020, 10, 27)')"
    assert repr(transaction) == expected


def test_positive_amount_str():
    """
    Test tests the result of __str__ method (positive amount)
    """
    transaction = Transaction(1234.56, datetime(2002, 1, 10))
    assert str(transaction) == "2002-01-10: +$1,234.56"

def test_negative_amount_str():
    """
    Test tests the result of __str__ method (negative amount)
    """
    transaction = Transaction(-17.25, datetime(2020, 1, 1))
    assert str(transaction) == "2020-01-01: -$17.25"

def test_account_deposit():
    """
    Test tests deposit method.
    Asserts that a deposit is added to the list of transactions
    """
    account = Account()
    account.deposit(100)
    transaction = Transaction(100)
    assert  account.transactions == [transaction]

def test_account_deposit_negative():
    """
    Tests deposit method accepts negative amount and converts it to positive
    """
    account = Account()
    account.deposit(-100)
    transaction = Transaction(100)
    assert account.transactions == [transaction]
def test_account_withdraw():
    """
    Asserts that a withdrawal is added to the list of transactions
    """
    account = Account()
    account.withdraw(-100)
    transaction = Transaction(-100)
    assert account.transactions == [transaction]
def test_account_withdraw_negative():
    """
    Asserts that a positive value is converted to negative
    """
    account = Account()
    account.withdraw(100)
    transaction = Transaction(-100)
    assert account.transactions == [transaction]
def test_get_balance_when_no_transactions():
    """
    When there are no transactions, 0 should be returned
    """
    account = Account()
    assert account.get_balance() == 0

def test_get_balance_returns_sum_of_transactions():
    """
    Asserts that get balance returns the sum of transactions
    """
    account = Account()
    account.deposit(100)
    account.withdraw(-50)
    assert account.get_balance() == 50
