
# Shell Sort involves sorting elements which are away from ech other. 
# We sort a large sublist of a given list and go on reducing the size
# of the list until all elements are sorted. 
# The below program finds the gap by equating it to half of the length
#  of the list size and then starts sorting all elements in it. 
# Then we keep resetting the gap until the entire list is sorted.

def shell_sort(lst):
    length = len(lst)
    gap = length//2

    while gap > 0:
        for i in range(gap,length):
            temp = lst[i]
            temp_index = i

            while temp_index >= gap and lst[temp_index-gap] > temp:
                lst[temp_index] = lst[temp_index-gap]
                temp_index = temp_index - gap
            
            lst[temp_index] = temp

        gap = gap//2
    return lst


if __name__ == "__main__":
    lst = [19,2,31,45,30,11,121,27]
    shell_sort(lst)