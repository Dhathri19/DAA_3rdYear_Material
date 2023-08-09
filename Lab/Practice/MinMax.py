def min_max_DC(A, i, j, min, max):
	if i == j:		 #If array has obly one element
		if min > A[j]:
			min = A[j]
		if max < A[i]:
			max = A[i]
		return min, max
	if j  == i - 1:	   #if array has 2 exact 2 elements
		if A[i] < A[j]:
			if min > A[i]:
				min = A[i]
			if max < A[j]:
				max = A[i]
		else:
			if min > A[j]:
				min = A[j]

			if max < A[i]:
				max = A[i]

		return min, max


	mid = (i + j) // 2
	min, max = min_max_DC(A, i, mid, min, max)
	min, max = min_max_DC(A, mid + 1, j, min, max)
	return min, max

INF = float('inf')
A=[]
c = int(input("Enter the number of values"))

for i in range(0,c):
    ele = int(input())
    A.append(ele)
print("Array :")
print(A)
(min, max) = (INF, -INF)
(min, max) = min_max_DC(A, 0, len(A) - 1, min, max)
print("\nMinimum:", min)
print("Maximum:", max)