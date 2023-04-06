"""  Реализация пользовательского списка """


class CustomList(list):
    """  Класс, реализующий пользовательский список. """

    def __add__(self, other):
        """  Левое сложение """
        res = CustomList([a+b for a, b in zip(self, other)])
        if len(other) > len(self):
            res += other[len(self):]
        if len(other) < len(self):
            res += self[len(other):]
        return res

    def __sub__(self, other):
        """ Левое вычитание """
        res = CustomList([a-b for a, b in zip(self, other)])
        if len(other) > len(self):
            res += [-i for i in other[len(self):]]
        if len(other) < len(self):
            res += self[len(other):]
        return res

    def __radd__(self, other):
        """ Правое сложение """
        return self + other

    def __rsub__(self, other):
        """ Правое вычитание """
        return CustomList([-i for i in self - other])

    def __eq__(self, other):
        """ Оператор равенства """
        return sum(self) == sum(other)

    def __ne__(self, other):
        """ Оператор неравенства """
        return sum(self) != sum(other)

    def __gt__(self, other):
        """ Оператор больше """
        return sum(self) > sum(other)

    def __ge__(self, other):
        """ Оператор больше или равно """
        return sum(self) >= sum(other)

    def __lt__(self, other):
        """ Оператор меньше """
        return sum(self) < sum(other)

    def __le__(self, other):
        """ Оператор меньше или равно """
        return sum(self) <= sum(other)

    def __str__(self):
        """ Метод, реализующий строковое представление CustomList. """
        items = ', '.join([str(i) for i in self])
        return f'items = [{items}], sum = {sum(self)}'
