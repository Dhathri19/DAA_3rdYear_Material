def merge_sort(arr):
    if(len(arr) > 1):
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)

        #Merge
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k = k + 1
    
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

print("Enter number of values:")
n = int(input())

print("Enter list to sort:")
lst = []
for i in range(0,n):
    ele = int(input())

    lst.append(ele)
print(lst)

merge_sort(lst)

print("Sorted array:")
print(lst)

