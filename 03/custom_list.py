"""Реализовать класс CustomList наследованием от list"""


class CustomList(list):

    def __add__(self, other):
        res = CustomList([a+b for a, b in zip(self, other)])
        if len(other) > len(self):
            res += other[len(self):]
        if len(other) < len(self):
            res += self[len(other):]
        return res

    def __sub__(self, other):
        res = CustomList([a-b for a, b in zip(self, other)])
        if len(other) > len(self):
            res += [-i for i in other[len(self):]]
        if len(other) < len(self):
            res += self[len(other):]
        return res

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return CustomList([-i for i in self - other])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        items = ', '.join([str(i) for i in self])
        return f'items = [{items}], sum = {sum(self)}'
