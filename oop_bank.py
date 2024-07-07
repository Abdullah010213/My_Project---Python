from bank_account import *

Abdullah = BankAccount(20000,"Abdullah")
Abdullah.get_balance()
Abdullah.deposit(10000)
Abdullah.withdrow(12345)

Azaam = BankAccount(100,"Azaam")
Abdullah.transfer_amount(2000,Azaam)

Luqmaan = InterestRewardAcc(20000,"Luqmaan")
Luqmaan.get_balance()
Luqmaan.deposit(1000)