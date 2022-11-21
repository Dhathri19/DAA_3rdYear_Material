#Taking inputs.
print("Enter number of values:")
n = int(input())
print("Enter value to search:")
value = int(input())
print("Enter list to search:")
lst = []
for i in range(0,n):
    ele = int(input())

    lst.append(ele)
print(lst)

#BinarySearch
low = 0
high = len(lst) - 1
mid = 0

print("Element found at:")
while low <= high:
    mid = (low + high)//2
    if(lst[mid] < value):
        low = mid + 1
    elif(lst[mid] > value):
        high = mid - 1
    else:
        return mid
    return -1