"""
Coding Exercise 4
user_entries = ['10', '19.1', '20']

Extend the given code so it prints out the sum of the numbers.

The output of your code should be as below:

49.1
"""

user_entries_new = [float(item) for item in user_entries]
user_entries_sum = sum(user_entries_new)
print(user_entries_sum) 