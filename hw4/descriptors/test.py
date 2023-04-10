"""Юниттесты для дескрипторов"""


import unittest

from descriptors import Integer, String, PositiveInteger, EvenInteger


class Data:
    """Класс для проверки дескрипторов"""
    num = Integer()
    name = String()
    price = PositiveInteger()
    amount = EvenInteger()

    def __init__(self, num=-5, name='Petya', price=1000, amount=4):
        self.num = num
        self.name = name
        self.price = price
        self.amount = amount


class DescriptorsTestClass(unittest.TestCase):
    """Класс тестов дескрипторов"""

    def test_correct(self):
        """ Правильное  """
        test_data = Data()
        self.assertEqual(test_data.num, -5)
        self.assertEqual(test_data.name, 'Petya')
        self.assertEqual(test_data.price, 1000)
        self.assertEqual(test_data.amount, 4)
        test_data.num = -28
        test_data.price = 1200
        test_data.name = 'Kolya'
        test_data.amount = 6
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)

        correct_dict = {'int': -28, 'str': 'Kolya', 'positive_int': 1200, 'even_int': 6}
        self.assertEqual(test_data.__dict__, correct_dict)

        test_data.num = -35
        correct_dict['int'] = -35
        self.assertEqual(test_data.__dict__, correct_dict)

    def test_incorrect(self):
        """ Неправильное использование дескрипторов """
        test_data = Data()
        test_data.num = -28
        test_data.price = 1200
        test_data.name = 'Kolya'
        test_data.amount = 6
        with self.assertRaises(Exception):
            test_data.num = 1.5
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)
        with self.assertRaises(Exception):
            test_data.num = 'qwerty'
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)
        with self.assertRaises(Exception):
            test_data.name = 1
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)
        with self.assertRaises(Exception):
            test_data.price = -1
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)
        with self.assertRaises(Exception):
            test_data.price = 100.5
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)
        with self.assertRaises(Exception):
            test_data.amount = 7
        self.assertEqual(test_data.num, -28)
        self.assertEqual(test_data.name, 'Kolya')
        self.assertEqual(test_data.price, 1200)
        self.assertEqual(test_data.amount, 6)


if __name__ == '__main__':
    unittest.main()
