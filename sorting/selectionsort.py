def selectionSort(A, size):
   
    for i in range(size):
        min = i

        for j in range(i + 1, size):
            if A[i] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]
        
list1 = [3,2,0,1,4,5]
size = len(list1)
selectionSort(list1, size)
print(list1)
