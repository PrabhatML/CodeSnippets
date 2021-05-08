import bubblesort
import unittest
from hypothesis import given, strategies as st


class TestIdempotentBubble_Sorter(unittest.TestCase):
    @given(list=st.lists(st.integers()))
    def test_idempotent_bubble_sorter(self, list):
        result = bubblesort.bubble_sorter(list=list)
        self.assertEqual(result, sorted(list))


if __name__ == '__main__':
    unittest.main()