import pytest
from src.bank_account import BankAccount

class TestBankAccount:

    @pytest.mark.parametrize("expression", [
        10,
        20,
        30,
    ])
    def test_empty_input(self, money):
        """Тест пустого ввода"""
        with pytest.raises(ValueError, match="Недостаточно денег"):
            acc = BankAccount("Alice", money)
            acc.deposit(200)
            acc.withdraw(10000)
            print(acc.get_balance())

   