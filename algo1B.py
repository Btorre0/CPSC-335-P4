from functools import lru_cache
## The Dynamic Programming Approach (Part B)
# This problem can also be solved using the dynamic programming approach.
# It uses a top-down dynamic programming to handle the overlapping subproblems.
# Since there are two changing values, the resultant amount and the current index,
# a two-dimensional array can be used to store the results of all the solved sub-problems.

# To calculate the maximum value obtainable with the selection of item 𝑖,
# a comparison of its cost is made with the total purchase capacity.

def dp_stock_maximization(M, items):
    n = len(items)
    # Create a 2D array to store the maximum value at each n and M
    dp = [[0 for _ in range(M + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, M + 1):
            if items[i - 1][1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][1]] + items[i - 1][0])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][M]

def dp(i, remaining):
    if i == 0 or remaining == 0:
        return 0
    result = dp(i + 1, remaining)
    cost = items[i][1]
    stocks = items[i][0]
    
# If item 𝑖 cost more than the available investment sum, it cannot be used.
# If a new candidate potentially increases the value of purchase and is less or
# equal to the maximum available sum, it is selected. The approach evaluates the highest 
# value of all possible subsets, then selects the subset with the highest value that is still
# under the weight limit.
    if cost <= remaining:
        result = max(result, dp(i + 1, remaining - cost) + stocks)
    return result


    