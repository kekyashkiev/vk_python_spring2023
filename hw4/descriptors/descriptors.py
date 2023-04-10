""" Модуль для дескрипторов с проверками типов и значений"""


class Integer:
    """Класс целых чисел"""
    def __init__(self, val=None, field_name='int'):
        self.val = val
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, int):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not int")


class String:
    """Класс строк"""
    def __init__(self, name=None, field_name='str'):
        self.name = name
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, str):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not str")


class PositiveInteger:
    """Класс положительных целых чисел"""
    def __init__(self, val=None, field_name='positive_int'):
        self.val = val
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, int) and (val > 0):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("not positive int")


class EvenInteger:
    """Класс четных чисел"""
    def __init__(self, val=None, field_name='even_int'):
        self.val = val
        self.field_name = field_name

    def __get__(self, obj, objtype):
        return getattr(obj, self.field_name)

    def __set__(self, obj, val):
        if isinstance(val, int) and (val % 2 == 0):
            setattr(obj, self.field_name, val)
        else:
            raise Exception("odd int")
