"""
Task 1: Validating Calculations
Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

Task 2: Mix and Match
Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.
"""

#Task 1: Validating Calculations
x = 5 + 5
y = (5 + 5)
print(x, y)

#Task 2: Mix and Match
a = 2
b = 3
c = (a or b) > 1 + 3
# With the order of operations, (a or b) will be seen as the first condition to check. Then, the comparison will check to see if either a or b is greater than the result of 1 + 3 which is 4. Neither a or b is greater than 4, therefore False.
print(c)