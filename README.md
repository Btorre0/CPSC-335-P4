# CPSC-335-P4

Spring 2025 CPSC 335 - Algorithm Engineering
Abstract
In this project, you will design, implement and analyze an exhaustive optimization and a dynamic programming algorithm for solving the same problem.

The Stock Purchase Maximization Problem
Given a fixed amount of purchasing power or financial resources, the problem seeks to maximize the number of stocks an investor may purchase. Future values of these stocks are not considered at the time of purchase.

This problem can be mathematically represented as:

![alt text](<Screenshot 2025-04-21 at 5.50.18 PM.png>)

Assume that you are given a set of stocks as an array of arrays. Each entry in the subarray represents a company, with the number of stocks available and the cumulative value of all available stocks. You are also given a specific sum of money to invest. Buying a fraction of any item is not allowed. Your task is to design an algorithm to determine the maximum number of stocks you are able to purchase. Your solution should give the indices of the array(stocks) to be selected. The cumulative value of all selected stocks must be equal or less than the given sum. The problem is similar to a well-known algorithmic optimization problem.

A sample is given below. It contains 4 items corresponding to company A, B, C and D. Each company has [𝑥, 𝑦] attributes, where 𝑥 = numbers of trading stocks and 𝑦 = monetary value of the trading stocks.

Sample input
Stocks_and_values = [ [1, 2], [3, 3], [5, 6], [6, 7] ]. Amount = 10

Sample Output = [10, [1,3] where 1 is the index of [3, 3] and 3 is the index of [6, 7]

The Exhaustive Optimization Approach (Part A)
An exhaustive optimization algorithm can be used to solve this problem. The approach evaluates the number of stocks and values of all possible subsets, and selects the subset with the highest value that is still under the available fund limit. It recomputes combination at each state. This approach provides an efficient, but expensive solution.

def stock_maximization (M, items):

best = None for candidates in <stocks_combinations>(items):

if verify_combinations(M, items, candidate):

if best is None or total_value(candidate) > total_value(best)

best = candidate return best

This approach was extensively discussed in class.

The Dynamic Programming Approach (Part B)
This problem can also be solved using the dynamic programming approach. It uses a top-down dynamic programming to handle the overlapping subproblems. Since there are two changing values, the resultant amount and the current index, a two-dimensional array can be used to store the results of all the solved sub-problems.

To calculate the maximum value obtainable with the selection of item 𝑖, a comparison of its cost is made with the total purchase capacity. If item 𝑖 cost more than the available investment sum, it cannot be used. If a new candidate potentially increases the value of purchase and is less or equal to the maximum available sum, it is selected. The approach evaluates the highest value of all possible subsets, then selects the subset with the highest value that is still under the weight limit.
