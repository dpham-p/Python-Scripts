# This program calculates the credit card balance after one year  if a person only pays the minimum monthly payment required by the credit card company each month.
# Input variables:    balance            - the outstanding balance on the credit card
#                     annualInterestRate - annual interest rate as a decimal
#                     monthlyPaymentRate - minimum monthly payment rate as a decimal

def unpaidBalance(balance,paid):
    # Inputs: int or float for balance and paid variables
    # Output: returns int or float for unpaid balance
    return balance - paid

def monthlyBalance(unpaidBal, interestRate):
    # Inputs: int or float for unpaidBal and interestRate variables
    # Output: returns int or float for monthly balance
    return unpaidBal + (interestRate/12.0) * unpaidBal

def minimumPayment(balance, minMonthlyPayRate):
    # Inputs: int or float for balance and minMonthlylPayRate variables
    # Output: returns int or float for minimum payment
    return balance * minMonthlyPayRate

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
min_pay = 0
unpaid_bal = 0

for month in range(1,13):
    min_pay = minimumPayment(balance,monthlyPaymentRate)
    unpaid_bal = unpaidBalance(balance,min_pay)
    balance = monthlyBalance(unpaid_bal, annualInterestRate)
    # print("Month " + str(month) + " Remaining balance: " + str(round(balance,2)))
print("Remaining balance: " + str(round(balance,2)))
                