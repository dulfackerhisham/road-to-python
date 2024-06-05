class BankAccount():
    def __init__(self,balance: float) -> None:
        self.balance = balance

    def deposit(self,dep: float):
        self.dep = dep
        self.balance = self.balance + self.dep
        print(f"you have deposited {self.dep} RS")

    def withdraw(self,with_draw: float):
        self.with_draw = with_draw
        self.balance = self.balance - self.with_draw
        print(f"you have withdrawed {self.with_draw} RS")

    def get_balance(self):
        print(f"your current balance is {self.balance} RS")

money_1 = BankAccount(50000.30)
money_1.deposit(2054.60)
money_1.get_balance()

money_1.withdraw(36000)
money_1.get_balance()