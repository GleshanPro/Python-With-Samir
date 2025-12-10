from src.log_method import log_method

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount
    
    @log_method
    def deposit(self, amount):
        self.balance += amount
        
    @log_method
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно денег")
    
    @log_method
    def get_balance(self):
        return self.balance
    
    @log_method
    @staticmethod
    def validate_amount(amount):
        if type(amount) != type(1):
            raise ValueError("Введена строка, а не число в качестве количества денег")
        if amount <= 0:
            raise ValueError("Отрицательное или нулевое количество денег")
        return True
    
