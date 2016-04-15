'''
Monthly interest rate = (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 4842 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal
monthlyPaymentRate = 0.04 # minimum monthly payment rate as a decimal

monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = monthlyPaymentRate * balance

totalPaid = 0

for month in range (1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance    
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    totalPaid += minimumMonthlyPayment 
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
    print "Remaining balance: " + str(round(balance, 2))
    
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))