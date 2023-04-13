"""Модуль для тестов"""


import unittest
import io
import sys
from CustomMeta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestMeta(unittest.TestCase):
    """Тесткейсы для метакласса"""
    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def test_meta(self):
        """добавление custom_ к немагическим атрибутам"""
        inst = CustomClass()
        self.assertTrue('custom_x' in CustomClass.__dict__)
        self.assertFalse('x' in CustomClass.__dict__)

        self.assertTrue('custom_line' in CustomClass.__dict__)
        self.assertFalse('line' in CustomClass.__dict__)

        """Сохранение имен магических атрибутов"""
        self.assertTrue('__str__' in CustomClass.__dict__)
        self.assertFalse('custom___str__' in CustomClass.__dict__)

        self.assertTrue('__init__' in CustomClass.__dict__)
        self.assertFalse('custom___init__' in CustomClass.__dict__)

        self.assertTrue('__dict__' in CustomClass.__dict__)
        self.assertFalse('custom___dict__' in CustomClass.__dict__)

        """изменение имен немагических атрибутов, неизменность самих атрибутов"""
        self.assertEqual(inst.__str__(), "Custom_by_metaclass")
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(inst.custom_x, 50)

        """изменение имен атрибутов, задаваемых в init и после init на имена с префиксом custom_"""
        self.assertTrue('custom_val' in inst.__dict__)
        self.assertFalse('val' in inst.__dict__)

        inst.field = 1
        self.assertTrue('custom_field' in inst.__dict__)
        self.assertFalse('field' in inst.__dict__)

        self.assertRaises(AttributeError, getattr, inst, 'val')
        self.assertRaises(AttributeError, getattr, inst, 'field')
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_field, 1)


if __name__ == "__main__":
    unittest.main()
