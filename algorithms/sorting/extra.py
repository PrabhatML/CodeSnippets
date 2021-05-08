

def partition(lst,low,high):
    i = low - 1
    pivot = lst[high]
    print(pivot,lst)
    for j in range(low,high):
        if lst[j] <= pivot:
            i += 1
            lst[j],lst[i] = lst[i],lst[j]
    lst[i+1],lst[high] = lst[high],lst[i+1]
    print(pivot,lst)
    return i+1

def quick_sort_divider(lst,low,high):
    print(low,high)
    if low < high:
        p = partition(lst,low,high)
        print(p)
        quick_sort_divider(lst,low,p-1)
        quick_sort_divider(lst,p+1,high)
    return lst


def quick_sort(lst):
    l = len(lst)
    quick_sort_divider(lst,0,l-1)
    return lst


lst = [32,1,123,23,6,77]
print(quick_sort(lst))