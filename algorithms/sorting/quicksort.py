#Quick sort

# The key process in quickSort is partition(). 
# Target of partitions is, given an array and an element x of array as pivot,
# put x at its correct position in sorted array 
# and put all smaller elements (smaller than x) before x, 
# and put all greater elements (greater than x) after x. 
# All this should be done in linear time.

def partition(lst,low,high):
    i = low-1
    #Pivot Element
    pivot = lst[high]
    for j in range(low,high):
        if lst[j] <= pivot:
            i = i+1
            lst[i],lst[j] = lst[j],lst[i]
        print(lst) 
        
    lst[i+1],lst[high] = lst[high],lst[i+1]
    return i+1    

def quick_sorter(lst,low,high):
    if low < high:
        pi = partition(lst,low,high)
        quick_sorter(lst,low,pi-1)
        quick_sorter(lst,pi+1,high)
    return lst

def quick_sort(lst):
    n = len(lst)
    return (quick_sorter(lst,0,n-1))


if __name__ == "__main__":
    lst = [2,5,3,9,6,8,4,7]
    print(quick_sort(lst))
