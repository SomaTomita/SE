# Encapsulation Example
# BAD PRACTICE:
# - Public attributes allow direct manipulation
# - No validation of data
# - No control over data access
# - Breaking encapsulation principles


class BadBankAccount:
    def __init__(self):
        self.balance = 0  # Public attribute
        self.transaction_history = []  # Public attribute
        self.interest_rate = 0.01  # Public attribute


# GOOD PRACTICE:
# - Private attributes with controlled access
# - Data validation
# - Proper audit trail
# - Business rules enforcement
# Benefits:
# 1. Data integrity
# 2. Security
# 3. Maintainability
# 4. Flexibility to change implementation


class BankAccount:
    def __init__(self, account_number):
        self.__balance = 0
        self.__account_number = account_number
        self.__transaction_history = []
        self.__interest_rate = 0.01
        self.__locked = False

    def deposit(self, amount):
        """Controlled way to add money with validation"""
        if self.__locked:
            raise ValueError("Account is locked")
        if self.__validate_amount(amount):
            self.__balance += amount
            self.__log_transaction("deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        """Controlled way to remove money with validation"""
        if self.__locked:
            raise ValueError("Account is locked")
        if self.__validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            self.__log_transaction("withdrawal", amount)
            return True
        return False

    def get_balance(self):
        """Safe way to check balance"""
        return self.__balance

    def get_transaction_history(self):
        """Return copy of transaction history"""
        return self.__transaction_history.copy()

    def __validate_amount(self, amount):
        """Private validation method"""
        return isinstance(amount, (int, float)) and amount > 0

    def __log_transaction(self, type_of_transaction, amount):
        """Private logging method"""
        self.__transaction_history.append(
            {"type": type_of_transaction, "amount": amount, "balance": self.__balance}
        )

    def get_account_number(self):
        """Safe way to access account number"""
        return self.__account_number


if __name__ == "__main__":
    # Create a bank account
    account = BankAccount("1234567890")

    # Test transactions
    account.deposit(1000)
    account.withdraw(300)
    account.deposit(500)
    account.withdraw(200)

    # Display account information
    print(f"Account Number: {account.get_account_number()}")
    print(f"Current Balance: ${account.get_balance()}")
    print("\nTransaction History:")
    for transaction in account.get_transaction_history():
        print(f"- {transaction}")

    # Try invalid operations
    try:
        account.withdraw(5000)  # Trying to withdraw more than balance
    except ValueError as e:
        print(f"\nError: {e}")

    #
    # These lines would raise AttributeError
    # ex)
    # print(account.__balance)  # Error: can't access private attribute
    # print(account.__transaction_history)  # Error: can't access private attribute
    # account.__balance = 1000000  # Error: can't modify private attribute

    # These operations would fail due to invalid inputs
    # ex)
    # account.deposit(-100)  # Error: negative deposit
    # account.withdraw(-50)  # Error: negative withdrawal
    # account.deposit("100")  # Error: non-numeric input

    # Example of trying to modify transaction history
    # ex)
    # history = account.get_transaction_history()
    # history.append("Fake transaction")  # Won't affect the private list


# Output:
# Account Number: 1234567890
# Current Balance: $1000
#
# Transaction History:
# - Deposit: $1000
# - Withdrawal: $300
# - Deposit: $500
# - Withdrawal: $200
#
# Error: Insufficient funds for withdrawal


############################################################################
import copy


class Person:
    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items


if __name__ == "__main__":
    number = 42
    text = "Hello"
    number_list = [1, 2, 3]

    # isinstance() examples
    print("isinstance() examples:")
    print(f"Is {number} an integer? {isinstance(number, int)}")  # True
    print(f"Is {text} a string? {isinstance(text, str)}")  # True
    print(f"Is {text} an integer? {isinstance(text, int)}")  # False
    print(f"Is {number_list} a list? {isinstance(number_list, list)}")  # True

    # copy examples
    print("\ncopy examples:")
    # 1. Simple assignment (reference)
    person1 = Person("Alice", 30, ["book", "laptop"])
    person2 = person1  # Creates a reference, not a copy

    # 2. Shallow copy
    person3 = copy.copy(person1)  # Creates a shallow copy

    # 3. Deep copy
    person4 = copy.deepcopy(person1)  # Creates a deep copy

    # Demonstrate the differences
    print("\nOriginal list:", person1.items)

    # Modifying through reference
    person2.items.append("phone")
    print("After modifying reference:", person1.items)  # Changes original

    # Modifying shallow copy
    person3.items.append("tablet")
    print("After modifying shallow copy:", person1.items)  # Changes original

    # Modifying deep copy
    person4.items.append("camera")
    print("After modifying deep copy:", person1.items)  # Doesn't change original
    print("Deep copy list:", person4.items)
