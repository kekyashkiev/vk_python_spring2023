import unittest

from custom_list import CustomList


def test_element_comparison(test_class, list1, list2):
    test_class.assertEqual(len(list1), len(list2))
    for i, j in enumerate(list1):
        test_class.assertEqual(j, list2[i])


class CustomListTestClass(unittest.TestCase):

    def test_comparison(self):
        list_sum_15 = CustomList([1, 2, 3, 4, 5])
        list_sum_15_ = CustomList([10, 1, 4])
        list_sum_18 = CustomList([2, 4, 12])

        self.assertTrue(list_sum_15_ == list_sum_15)
        self.assertFalse(list_sum_15 == list_sum_18)
        self.assertFalse(list_sum_15_ == list_sum_18)

        self.assertTrue(list_sum_15 != list_sum_18)
        self.assertFalse(list_sum_15 != list_sum_15_)

        self.assertFalse(list_sum_15 > list_sum_18)
        self.assertTrue(list_sum_18 >= list_sum_15_)
        self.assertFalse(list_sum_18 < list_sum_15)
        self.assertFalse(list_sum_18 <= list_sum_15)

    def test_str(self):
        custom_list = CustomList([1, 2, 3, 4])
        self.assertEqual(str(custom_list), "items = [1, 2, 3, 4], sum = 10")

        custom_list = CustomList([1])
        self.assertEqual(str(custom_list), "items = [1], sum = 1")

        custom_list = CustomList([])
        self.assertEqual(str(custom_list), "items = [], sum = 0")

    def test_sum_custl_list(self):
        # a + b: len(a) == len(b)
        list_1 = CustomList([1, 2])
        list_2 = [3, 4]
        sum_result = list_1 + list_2
        true_result = CustomList([4, 6])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2])
        test_element_comparison(self, list_2, [3, 4])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) < len(b)
        list_1 = CustomList([1, 2])
        list_2 = [3, 4, 5]
        sum_result = list_1 + list_2
        true_result = CustomList([4, 6, 5])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2])
        test_element_comparison(self, list_2, [3, 4, 5])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) > len(b)
        list_1 = CustomList([1, 2])
        list_2 = [3]
        sum_result = list_1 + list_2
        true_result = CustomList([4, 2])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2])
        test_element_comparison(self, list_2, [3])
        self.assertEqual(type(sum_result), CustomList)

    def test_sum_list_custl(self):
        # a + b: len(a) == len(b)
        list_1 = [1, 2, 3, 4]
        list_2 = CustomList([5, 6, 7, 8])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 12])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7, 8])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) < len(b)
        list_1 = [1, 2, 3, 4]
        list_2 = CustomList([5, 6, 7, 8, 9])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 12, 9])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7, 8, 9])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) > len(b)
        list_1 = [1, 2, 3, 4]
        list_2 = CustomList([5, 6, 7])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 4])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7])
        self.assertEqual(type(sum_result), CustomList)

    def test_sum_custl_custl(self):
        # a + b: len(a) == len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = CustomList([5, 6, 7, 8])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 12])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7, 8])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) < len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = CustomList([5, 6, 7, 8, 9])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 12, 9])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7, 8, 9])
        self.assertEqual(type(sum_result), CustomList)

        # a + b: len(a) > len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = CustomList([5, 6, 7])
        sum_result = list_1 + list_2
        true_result = CustomList([6, 8, 10, 4])
        test_element_comparison(self, sum_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, [5, 6, 7])
        self.assertEqual(type(sum_result), CustomList)

    def test_dif_custl_custl(self):
        # a - b: len(a) == len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = CustomList([5, 6, 7, 8])
        dif_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, -4])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3, 4]))
        test_element_comparison(self, list_2, CustomList([5, 6, 7, 8]))
        self.assertEqual(type(dif_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = CustomList([5, 6, 7])
        sub_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, 4])
        test_element_comparison(self, sub_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3, 4]))
        test_element_comparison(self, list_2, CustomList([5, 6, 7]))
        self.assertEqual(type(sub_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = CustomList([1, 2, 3])
        list_2 = CustomList([4, 5, 6, 7])
        dif_result = list_1 - list_2
        true_result = CustomList([-3, -3, -3, -7])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3]))
        test_element_comparison(self, list_2, CustomList([4, 5, 6, 7]))
        self.assertEqual(type(dif_result), CustomList)

    def test_dif_custl_list(self):
        # a - b: len(a) == len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = [5, 6, 7, 8]
        dif_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, -4])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3, 4]))
        test_element_comparison(self, list_2, [5, 6, 7, 8])
        self.assertEqual(type(dif_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = CustomList([1, 2, 3, 4])
        list_2 = [5, 6, 7]
        dif_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, 4])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3, 4]))
        test_element_comparison(self, list_2, [5, 6, 7])
        self.assertEqual(type(dif_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = CustomList([1, 2, 3])
        list_2 = [4, 5, 6, 7]
        dif_result = list_1 - list_2
        true_result = CustomList([-3, -3, -3, -7])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, CustomList([1, 2, 3]))
        test_element_comparison(self, list_2, [4, 5, 6, 7])
        self.assertEqual(type(dif_result), CustomList)

    def test_dif_list_custl(self):
        # a - b: len(a) == len(b)
        list_1 = [1, 2, 3, 4]
        list_2 = CustomList([5, 6, 7, 8])
        dif_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, -4])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, CustomList([5, 6, 7, 8]))
        self.assertEqual(type(dif_result), CustomList)

        # a - b: len(a) > len(b)
        list_1 = [1, 2, 3, 4]
        list_2 = CustomList([5, 6, 7])
        dif_result = list_1 - list_2
        true_result = CustomList([-4, -4, -4, 4])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3, 4])
        test_element_comparison(self, list_2, CustomList([5, 6, 7]))
        self.assertEqual(type(dif_result), CustomList)

        # a - b: len(a) < len(b)
        list_1 = [1, 2, 3]
        list_2 = CustomList([4, 5, 6, 7])
        dif_result = list_1 - list_2
        true_result = CustomList([-3, -3, -3, -7])
        test_element_comparison(self, dif_result, true_result)
        test_element_comparison(self, list_1, [1, 2, 3])
        test_element_comparison(self, list_2, CustomList([4, 5, 6, 7]))
        self.assertEqual(type(dif_result), CustomList)


if __name__ == '__main__':
    unittest.main()
