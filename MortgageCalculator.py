#!usr/bin/python


# Mortgage Formulars
# Monthly Payment = L * (R * (1 + R)^N) / ((1 + R)^N - 1)
# where,
# L = Loan amount,
# R = monthly interest rate = annual rate / 12,
# N = total number of months
#
# Caculate Remaining Loan Balance after P months
# = L * ((1 + R)^N - (1 + R)^P) / ((1 + R)^N - 1)


class Mortgage:
    def __init__(self, amount, months, annualRate):
        self._amount = int(amount)
        self._months = int(months)
        self._monthRate = float(annualRate / 1200)

    def getMonthlyPayment(self):
        payment = float(self._amount * self._monthRate) / \
            (1.0 - 1.0 / (1.0 + self._monthRate) ** self._months)
        return payment

    def getTotalPay(self):
        return self.getMonthlyPayment() * self._months

    def getTotalInterest(self):
        return self.getTotalPay() - self._amount

    def getRemainingBalance(self, months):
        rate = 1 + self._monthRate
        balance = self._amount * (rate**self._months - rate**months) / \
            (rate**self._months - 1)
    
    def printSummary(self):
        print('{0:>25s}:  {1:>12.2f}'.format('Amount', self._amount))
        print('{0:>25s}:  {1:>12.2f}'.format('Monthly Payment', self.getMonthlyPayment()))
        print('{0:>25s}:  {1:>12.2f}'.format('Total Payout', self.getTotalPay()))
        print('{0:>25s}:  {1:>12.2f}'.format('Total Interest', self.getTotalInterest()))
    
if __name__ == '__main__':
    mon = 30 * 12
    cash = 60000
    
    Loan1 = 520000
    LoanBal1 = 514837
    rate1old = 3.25
    rate1new = 2.75
    close1 = 3400
    intPaid1 = 8837.66

    mort1orig = Mortgage(Loan1, mon, rate1old)
    intBal1 = mort1orig.getTotalInterest() - intPaid1
    print("Loan 1 int bal = " + '{0:.2f}'.format(intBal1))

    Loan2 = 140000
    LoanBal2 = 137655
    rate2old = 4.75
    rate2new = 3.5
    close2 = 2900
    intPaid2 = 7499.96

    mort2orig = Mortgage(Loan2, mon, rate2old)
    intBal2 = mort2orig.getTotalInterest() - intPaid2
    print("Loan 2 int bal = " + '{0:.2f}'.format(intBal2))

    
    for i in range(0, cash + 1):
        bal1 = LoanBal1 - i
        mort1old = Mortgage(bal1, mon, rate1old)
        mort1new = Mortgage(bal1, mon, rate1new)

        bal2 = LoanBal2 - (cash - i)
        mort2old = Mortgage(bal2, mon, rate2old)
        mort2new = Mortgage(bal2, mon, rate2new)

