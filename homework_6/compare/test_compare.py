import unittest
import random
from compare import MergeSort, QuickSort

### Конкретно здесь получились случаи, когда QuickSort работает не так медленно из-за реализации выбора опорного элемента. 
### Если брать опорный элемент как первый или последний, то на отсортированных и обратно отсортированных данных QuickSort будет работать значительно медленнее

class TestSortingPerformance(unittest.TestCase):
    def setUp(self):
        self.random_list = [random.randint(0, 1000) for _ in range(100000)]
        self.sorted_list = list(range(100000))
        self.reversed_list = list(range(100000))[::-1]

    def test_random_input(self):
        '''
        Оба примерно одинаково по времени
        '''
        qs_result = QuickSort(self.random_list.copy())
        ms_result = MergeSort(self.random_list.copy())
        self.assertEqual(qs_result, sorted(self.random_list))
        self.assertEqual(ms_result, sorted(self.random_list))

    def test_sorted_input(self):
        '''
        QuickSort должен работать медленнее
        '''
        qs_result = QuickSort(self.sorted_list.copy())
        ms_result = MergeSort(self.sorted_list.copy())
        self.assertEqual(qs_result, sorted(self.sorted_list))
        self.assertEqual(ms_result, sorted(self.sorted_list))

    def test_reversed_input(self):
        '''
        QuickSort должен работать медленнее
        '''
        qs_result = QuickSort(self.reversed_list.copy())
        ms_result = MergeSort(self.reversed_list.copy())
        self.assertEqual(qs_result, sorted(self.reversed_list))
        self.assertEqual(ms_result, sorted(self.reversed_list))

if __name__ == "__main__":
    unittest.main()
