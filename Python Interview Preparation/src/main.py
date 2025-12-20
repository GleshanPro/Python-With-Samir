from src.bank_account import BankAccount

def main():
    acc = BankAccount("Alice", 1000)
    acc.deposit(200)
    acc.withdraw(50)
    print(acc.get_balance())

if __name__ == "__main__":
    main()