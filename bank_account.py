class BlanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,name):
        self.balance = initial_amount
        self.name = name
        print("---------ABD Bank of World---------\n***********************************")
        print(f"Welcome Mr.{self.name}\nYour Balance : ${self.balance:.2f}")
        print("====================================")

    def get_balance(self):
        print(f"Account : {self.name}\nBlance : ${self.balance:.2f}")
        print("====================================")

    def deposit(self,deposit_money):
        self.balance = self.balance + deposit_money
        print("Your Deposit Completed...")
        self.get_balance()

    def viable_transection(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BlanceException(f"\nSorry..., Account : {self.name} only has a balance ${self.balance:.2f}")
        
    def withdrow(self,amount):
        try:
            self.viable_transection(amount)
            self.balance = self.balance - amount
            print("Your Withdrow Completed...")
            self.get_balance()
        except BlanceException as error:
            print(f"Withdrow interruped : {error}")

    def transfer_amount(self,amount,account):
        try:
            print("Beginning Transfer...")
            self.viable_transection(amount)
            self.withdrow(amount)
            account.deposit(amount)
            print("Transfer Completed...")
        except BlanceException as error:
            print(f"Transfer interruped : {error}")

class InterestRewardAcc(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount*1.05)
        print("Your Deposit Completed...")
        self.get_balance()

class SavingAcc(InterestRewardAcc):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5
    
    def withdrow(self,amount):
        try:
            self.viable_transection(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Your Withdrow Completed...")
            self.get_balance()
        except BlanceException as error:
            print(f"Withdrow interruped : {error}")
