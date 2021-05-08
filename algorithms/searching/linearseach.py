# def linearsearch(lst,ele):
#     count = 0
#     match = False

#     while count < len(lst) and match == False:
#         if lst[count] == ele:
#             return count
#         else:
#             count += 1
#     return -1


def linearsearch(arr,val):
    
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

lst = [21,43,12,11,5,8]
print(linearsearch(lst,12))