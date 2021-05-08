# Merge sort first divides the array into equal halves and
#  then combines them in a sorted manner.

def merge_sorter(unsorted_list):
    l = len(unsorted_list)
    if l <= 1:
        return unsorted_list
    m = l//2
    left_list = unsorted_list[:m]
    right_list = unsorted_list[m:]

    left_list = merge_sorter(left_list)
    right_list = merge_sorter(right_list)

    return list(merge(left_list,right_list))

def merge(left_list,right_list):
    res = []
    while  len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list.pop(0))
        else:
            res.append(right_list.pop(0))
    if len(left_list) == 0:
        res += right_list
    else:
        res += left_list
    return res


if __name__ == '__main__':
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sorter(unsorted_list))