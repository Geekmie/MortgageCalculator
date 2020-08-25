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

    L1 = 500000
    r1 = 2.75
    m1 = Mortgage(L1, mon, r1)
    close1 = 3400

    L2 = 100000
    r2 = 3.5
    m2 = Mortgage(L2, mon, r2)
    close2 = 2900

    m1.printSummary()
    m2.printSummary()
