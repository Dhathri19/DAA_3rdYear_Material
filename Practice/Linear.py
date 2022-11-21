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

#Implementing linear search

pos = -1
for i in range(0,len(lst)):
    if(lst[i] == value):
        #print("Ele found")
        pos = i
    else:
        i = i + 1
    
if(pos == -1):
    print("Element not found")
else:
    print("Position is:")
    print(pos)