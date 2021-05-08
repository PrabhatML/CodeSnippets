def mergesortedarray(arr1,arr2,l1,l2):
    arr3 = [None] * (l1 + l2)
    i = 0
    j = 0
    k = 0

    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1

    while i < l1:
        arr3[k] = arr1[i]
        k += 1
        i += 1

    while j < l2:
        arr3[k] = arr2[j]
        k += 1
        j += 1
    
    for i in range(len(arr3)):
        print(i)


arr1 = [1,3,5,7]
arr2 = [2,4,6,8]

n1 = len(arr1)
n2 = len(arr2)

(mergesortedarray(arr1,arr2,n1,n2))