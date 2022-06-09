class Atm:
    def __init__(self,cardnumber,pin,balance):
        self.cardnumber=cardnumber
        self.pin=pin 
        self.balance=balance 

    def balanceenquiry(self):
        print(self.balance)

    def cashwithdrawl(self,amount):
        self.balance=self.balance-amount 
        print(self.balance)
    
user=Atm(227,1806,5000000)
user.balanceenquiry()
user.cashwithdrawl(1000000)