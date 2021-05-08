def  maxSubArraySum(a,size):
    max_so_far = a[0]
    current_max = a[0]

    for i in range(1,size):
        current_max = max(a[i],current_max+a[i])
        max_so_far = max(max_so_far,current_max)
    
    return max_so_far


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a,len(a)))