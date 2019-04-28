# This program calculates the lowest payment per month for one year to pay off the balance.
# Input variables:    balance            - the outstanding balance on the credit card
#                     annualInterestRate - annual interest rate as a decimal

def unpaidBalance(balance,paid):
    # Inputs: int or float for balance and paid variables
    # Output: returns int or float for unpaid balance
    return balance - paid

def monthlyBalance(unpaidBal, interestRate):
    # Inputs: int or float for unpaidBal and interestRate variables
    # Output: returns int or float for monthly balance
    return unpaidBal + (interestRate/12.0) * unpaidBal

unpaid_Bal = balance
payment = 10
month = 1
while unpaid_Bal >= 0:
    
    for month in range(1,13):
        unpaid_Bal = unpaidBalance(unpaid_Bal,payment)
        unpaid_Bal = monthlyBalance(unpaid_Bal, annualInterestRate)
    if unpaid_Bal > 0:
        payment += 10
        month = 0
        unpaid_Bal = balance
print("Lowest Payment: " + str(payment))