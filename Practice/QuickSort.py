def quick_sort(arr, left, right):
    if left < right:
        partiton_pos = partiton(arr, left, right)
        quick_sort(arr, left, partiton_pos - 1)
        quick_sort(arr, partiton_pos + 1, right)

def partiton(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i = i + 1
        while j > left and arr[j] >= pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
        
print("Enter number of values:")
n = int(input())

print("Enter list to sort:")
lst = []
for i in range(0,n):
    ele = int(input())

    lst.append(ele)
print(lst)

quick_sort(lst, 0, len(lst) - 1)

print("Sorted array:")
print(lst)

