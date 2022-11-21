def knapSack(W, wt, val, n):
    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here
    if n == 0 or W == 0:
        return 0
    if wt[n-1] <= W:
        return (max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1)))
    else:
        return (knapSack(W, wt, val, n-1))

print("Enter number of values:")
n = int(input())

print("Enter the capacity:")
W = int(input())

print("Enter the profits:")
val = []
for i in range(0,n):
    ele = int(input())

    val.append(ele)
print(val)

print("Enter the weights:")
wt = []
for i in range(0,n):
    ele = int(input())

    wt.append(ele)
print(wt)

print(knapSack(W, wt, val, n))
