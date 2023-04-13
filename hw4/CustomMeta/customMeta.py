"""Модуль, добавляющий префикс custom"""


class CustomMeta(type):
    """Реализация метакласса"""
    def __setattr__(cls, key, value):
        new_name = "custom_" + key
        object.__setattr__(cls, new_name, value)

    def __new__(cls, name, bases, classdict):
        attrs = ((name, value) for name, value in classdict.items() if
                 not (name.startswith('__') and name.endswith('__')))
        custom_attr = dict(("custom_" + name, value) for name, value in attrs)
        attrs = ((name, value) for name, value in classdict.items() if
                 (name.startswith('__')) and name.endswith('__'))
        custom_attr.update(attrs)
        custom_attr['__setattr__'] = cls.__setattr__
        return super().__new__(cls, name, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


Example = CustomClass()
""" экземпляр CustomClass """
