# bank_account.py

class InsufficientFundsError(Exception):
    """Raised when attempting to withdraw more than the available balance."""
    pass


class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        # encapsulate the balance using a "protected" attribute
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self._balance:
            self._balance -= float(amount)
            return True
        # do not change balance on failure
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self._balance:.2f}")

    @property
    def balance(self) -> float:
        """Read-only access to the current balance for tests or other code."""
        return self._balance
