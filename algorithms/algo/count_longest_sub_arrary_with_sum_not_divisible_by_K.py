from collections import defaultdict

k = 3

def count_longest_sub_arrary_with_sum_not_divisible_by_K(arr):
    if sum(arr)%3 != 0:
        return 1
    else:
        L = 0
        R = 0
        l =  len(arr)
        for i in range(0,l):
            if arr[i]%3!=0:
                L = i
                break
        for i in range(l-1,0,-1):
            if arr[i]%3!=0:
                R = i
                break
        total,count = 0,0

        if (L==l):
            return -1
        else:
            length = max(l-L-1,R)

        for i in range(length):
            total += arr[i]
        
        if total%k!=0:
            count+=1
        print(total)
        for i in range(length,l):
            total = total + arr[i]
            print(total)
            total = total + arr[i-length]
            print(i,i-length)
            print(total)
            if total%k!=0:
                count += 1
        return count

arr = [2, 4, 3, 5, 1]
print(count_longest_sub_arrary_with_sum_not_divisible_by_K(arr))
