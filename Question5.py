def mergeSort(array):
    if len(array) > 1: 
        r = len(array)//2
        L = array[:r]
        M = array[r:] 
        mergeSort(M) 
        mergeSort(L)
        i = j = k = 0 
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
# Usage
if __name__ == '__main__':
    array = list(input('sth:'))

    mergeSort(array)
    print("Sorted array is: ")
    printList(array)
