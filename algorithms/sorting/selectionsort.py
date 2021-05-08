# In selection sort we start by finding the minimum 
# value in a given list and move it to a sorted list. 
# Then we repeat the process for each of the remaining 
# elements in the unsorted list. 
# The next element entering the sorted list is compared with 
# the existing elements and placed at its correct position. 
# So at the end all the elements from the unsorted list are sorted.

def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        min_ind = i
        for j in range(i+1,length):
            if lst[min_ind] > lst[j]:
                min_ind = j
        lst[i],lst[min_ind] = lst[min_ind],lst[i]
    
    return lst

if __name__ == "__main__":
    lst = [12,3,1,2,43,13,77]
    print(selection_sort(lst))