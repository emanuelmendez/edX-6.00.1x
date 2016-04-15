###########################

balance = 3926 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal

##########################

monthlyInterestRate = annualInterestRate / 12.0
minFixedMonthlyPayment = 10
unpaidBalance = balance
month = 1

while unpaidBalance > 0:
    if month <= 12:
        monthlyUnpaidBalance = unpaidBalance - minFixedMonthlyPayment
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    else:
        if unpaidBalance > 0:
            minFixedMonthlyPayment += 10
            month = 1
            unpaidBalance = balance
        elif unpaidBalance < 0:
            minFixedMonthlyPayment -= 10
            month = 1
            unpaidBalance = balance
        else:
            break
            
print "Lowest payment: " + str(minFixedMonthlyPayment)