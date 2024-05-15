"""
Task 1: Grocery Store Math
Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic

Task 2: Bank Interest
If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.
"""

#Task 1: Grocery Store Math

bread, peanut_butter, jelly = 2.00, 3.00, 4.00
total = bread + peanut_butter + jelly
print(total)

#Task 2: Bank Interest

savings_account = 10000.00
interest_rate = .07
apy = savings_account * interest_rate
print(savings_account + apy)
