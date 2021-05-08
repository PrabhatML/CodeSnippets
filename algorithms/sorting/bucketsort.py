#Bucket Sort
def  insertion_sort(b):
    for i in range(1,len(b)):
        j = i -1
        next_ele = b[i]

        while b[j] > next_ele and j >= 0:
            b[j+1] = b[i]
            j = j -1
        b[j+1] = next_ele
    return b
def bucket_sort(lst):
    arr = []
    slot_num = 10

    for i in range(slot_num):
        arr.append([])
    print(arr)

    for j in lst:
        index_b = int(slot_num*j)
        arr[index_b].append(j)
    print(arr)

    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return lst

if __name__ == "__main__":
    x = [0.0012,0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(bucket_sort(x))