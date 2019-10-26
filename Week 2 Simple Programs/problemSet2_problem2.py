# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:44:44 2017

@author: Mayur
"""
"""
Problem 2 - Paying Debt Off in a Year

Write a program that calculates the minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay 
off all debt in under 1 year, for example:

Lowest Payment: 180
 
Assume that the interest is compounded monthly according to the balance at the 
end of the month (after the payment for that month is made). The monthly payment 
must be a multiple of $10 and is the same for all months. Notice that it is possible 
for the balance to become negative using this payment scheme, which is okay. A 
summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + 
                             (Monthly interest rate x Monthly unpaid balance)
"""

#code
def minMonthlyPayment(balance, annualInterestRate):
  """
  input: balance at the start of month
         annualInterestRate
  output: minMonthlyPayment  
  """
  minMonthly = 0
  bal = balance
  while bal >= 0:
    N = 12
    minMonthly += 10
    bal = balance
    while N > 0:
      bal = bal - minMonthly
      bal = bal + (annualInterestRate/12)*bal
      N =  N - 1
  return minMonthly
#balance = 4773
#annualInterestRate = 0.2
minMonthly = minMonthlyPayment(balance, annualInterestRate)
print("Lowest Payment:",minMonthly)