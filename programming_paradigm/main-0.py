# main-0.py
import sys
from bank_account import BankAccount

def main():
    # change initial balance as needed for testing
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = None
    if params and params[0] != '':
        try:
            amount = float(params[0])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
