def subarraysum(arr,n):
    result = 0
    for i in range(0,n):
        temp = 0
        for j in range(i,n):
            print(i,j,arr[j])
            temp += arr[j]
            result += temp
    return result


arr = [ 1,2,3]
n = len(arr)
print(subarraysum(arr,n))