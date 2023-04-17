import unittest
from custom_meta import CustomClass


def func(var):
    return var.upper() if var.startswith('ddd') else var


class TestMeta(unittest.TestCase):

    def test_add_custom_for_methods_and_cls_attr(self):
        tmp = CustomClass(1, 2, 3)
        self.assertEqual(getattr(tmp, 'custom_line')(), 100)

        self.assertTrue(hasattr(CustomClass, 'custom_public'))
        self.assertTrue(hasattr(CustomClass, '_custom_protected'))
        self.assertTrue(hasattr(CustomClass, '_custom_CustomClass__private'))
        self.assertTrue(hasattr(CustomClass, 'custom_line'))
        self.assertTrue(hasattr(CustomClass, '__str__'))

        self.assertFalse(hasattr(CustomClass, 'public'))
        self.assertFalse(hasattr(CustomClass, '_protected'))
        self.assertFalse(hasattr(CustomClass, '_CustomClass__private'))
        self.assertFalse(hasattr(CustomClass, 'line'))

        string = "ddd variable"
        tmp.func = func

        self.assertIsInstance(string, str)
        self.assertTrue(getattr(tmp, 'custom_func')(string), "DDD VARIABLE")
        self.assertEqual(getattr(tmp, 'custom_val'), 1)
        self.assertEqual(getattr(tmp, '_custom_val'), 2)
        self.assertEqual(getattr(tmp, '_custom_CustomClass__val'), 3)

        with self.assertRaises(AttributeError):
            self.assertEqual(getattr(tmp, 'val'), 1)

        with self.assertRaises(AttributeError):
            self.assertEqual(getattr(tmp, '_val'), 2)

        with self.assertRaises(AttributeError):
            self.assertEqual(getattr(tmp, '_CustomClass__val'), 3)


if __name__ == '__main__':
    unittest.main()
