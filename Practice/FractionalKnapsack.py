def knapsack(capacity, weights, profits, n):
    if(n == 0 or capacity == 0):
        return 0
    if(weights[n-1] > capacity):
        return knapsack(capacity, weights, profits, n-1)
    else:
        return max(profits[n-1] + knapsack(capacity - weights[n-1], weights, profits, n-1), knapsack(capacity, weights, profits, n - 1))


print("Enter number of values:")
n = int(input())

print("Enter the capacity:")
capacity = int(input())

print("Enter the profits:")
profits = []
for i in range(0,n):
    ele = int(input())

    profits.append(ele)
print(profits)

print("Enter the weights:")
weights = []
for i in range(0,n):
    ele = int(input())

    weights.append(ele)
print(weights)

print(knapsack(capacity, weights, profits, n))
