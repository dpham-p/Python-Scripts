# This program uses bisectional search to calculate the lowest payment per month for one year to pay off the balance.
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

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
unpaidBal = balance
monthlyBal = balance
payment_upper = balance * ((1 + monthlyInterestRate)**12)/12.0
payment_lower = balance / 12.0
payment = (payment_upper + payment_lower) / 2

while abs(unpaidBal) >= 0.01:
    unpaidBal = balance
    for month in range(1,13):
        unpaidBal = unpaidBalance(unpaidBal,payment)
        unpaidBal = monthlyBalance(unpaidBal, annualInterestRate)
    if unpaidBal > 0:
        payment_lower = payment
        payment = (payment_upper + payment_lower) / 2
    else:
        payment_upper = payment
        payment = (payment_upper + payment_lower) / 2
payment = round(payment,2)
print("Lowest Payment: " + str(payment))