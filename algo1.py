from itertools import combinations

def cost(candidates):
    return sum(item[1] for item in candidates)

def stocks(candidates):
    return [item[0] for item in candidates]

def verify_combinations(M, candidate):
    return cost(candidate) <= M

def stock_maximization (M, items):
    best = []
    n = items
    
    for r in range(1, n + 1):
        for combination in combinations(items, r):
            if verify_combinations(M, combination):
                if sum(item[1] for item in combination) > sum(item[1] for item in best):
                    best = combination
    return best

Stocks_and_values = [ [1, 2], [3, 3], [5, 6], [6, 7] ]
target = 10

result = stock_maximization(Stocks_and_values, target)
cost_value = cost(result)
# Sample Output = [10, [1,3] where 1 is the index of [3, 3] and 3 is the index of [6, 7]
print("Output = [", result, "where 1 is the index of ", Stocks_and_values[1], "and 3 is the index of ", Stocks_and_values[3], "]")