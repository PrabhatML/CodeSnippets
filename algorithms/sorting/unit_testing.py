import unittest
import HtmlTestRunner
from hypothesis import given
import hypothesis.strategies as st
from bubblesort import bubble_sorter
from mergesort import merge_sorter
from insertsort import insertion_sort
from shellsort import shell_sort
from selectionsort import selection_sort
from quicksort import quick_sort

class SimpleTest(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_bubblesort(self,lst):
        self.assertEqual(bubble_sorter(lst),sorted(lst))

    @given(st.lists(st.integers()))
    def test_mergesort(self,lst):
        self.assertEqual(merge_sorter(lst),sorted(lst))

    @given(st.lists(st.integers()))
    def test_insertionsort(self,lst):
        self.assertEqual(insertion_sort(lst),sorted(lst))

    @given(st.lists(st.integers()))
    def test_shellsort(self,lst):
        self.assertEqual(shell_sort(lst),sorted(lst))

    @given(st.lists(st.integers()))
    def test_selectionsort(self,lst):
        self.assertEqual(selection_sort(lst),sorted(lst))

    @given(st.lists(st.integers()))
    def test_quicksort(self,lst):
        self.assertEqual(quick_sort(lst),sorted(lst))


if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='testing_reports',combine_reports=True,verbosity=2,report_name='unit_test_sorting',add_timestamp=False))