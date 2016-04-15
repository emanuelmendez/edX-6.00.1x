###########################

# Testing:

balance = 492732 # the outstanding balance on the credit card
annualInterestRate = 0.15 # annual interest rate as a decimal

##########################

def bisect_search (low_bound, up_bound, unpaidBalance):
    month = 1
    for month in range (1, 13):
        monthlyUnpaidBalance = unpaidBalance - ((low_bound + up_bound) / 2.0)
        unpaidBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 3)
        month += 1
        
    if unpaidBalance > 0:
        return bisect_search (((low_bound + up_bound) / 2), up_bound, balance)
    elif unpaidBalance < 0:
        return bisect_search (low_bound, ((low_bound + up_bound) / 2), balance)
    else:
        return round(low_bound, 2)

monthlyInterestRate = annualInterestRate / 12.0
low = balance / 12.0
upp = (balance * (1 + monthlyInterestRate)**12 ) / 12.0

print "Lowest payment: " + str(bisect_search(low, upp, balance))