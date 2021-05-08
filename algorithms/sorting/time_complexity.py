import random
from utils import execution_time
from bubblesort import bubble_sorter
from mergesort import merge_sorter
from insertsort import insertion_sort
from shellsort import shell_sort
from selectionsort import selection_sort
from quicksort import quick_sort

lst = random.sample(range(0,100000),40000)
function_lst = [merge_sorter,insertion_sort,shell_sort,bubble_sorter,selection_sort]

for f in function_lst:
    f = execution_time(f)
    f(lst)
