def binarysearch(lst,ele):
    low = mid = 0
    high = len(lst)-1

    while low <= high:
        mid = (high+low)//2

        if lst[mid]< ele:
            low = mid + 1
        
        elif lst[mid] > ele:
            high = mid + 1

        else:
            return mid
    
    return -1


lst = [12,1,32,4,66,443,23,2]
lst = sorted(lst)
ele = 32
result = binarysearch(lst,ele)
print(result)