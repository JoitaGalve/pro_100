class ATM(object):
    def __init__(self, atmCardNumber, password):
        self.atmCardNumber = atmCardNumber
        self.password = password

    def cashWithdrawl(self):
        print("Cash Withdrawn")

    def moneyDeposited(self):
        print("Money Deposited")

    def balanceEnquiry(self):
        print("Balance Enquiry")

joita = ATM(45678, 1234)
geetika = ATM(90786, 2314)

joita.cashWithdrawl()
print(joita.atmCardNumber)
print(joita.password)
geetika.moneyDeposited()
geetika.balanceEnquiry()