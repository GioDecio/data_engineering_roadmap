"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
 the ith customer has in the jth bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
"""


def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
    return max(wealth, max_wealth)


accounts = [[1, 2, 3], [3, 2, 1]]
print(maximum_wealth(accounts))
