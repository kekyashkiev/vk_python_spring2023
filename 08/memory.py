import cProfile
import time
import weakref
from memory_profiler import profile
from lru_cache import LRUCache


class Rectangle:
    """class without slots"""
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color


class RectangleSlot:
    """class with slots"""
    __slots__ = ("length", "width", "color")

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color


def make_cache():
    """initialization of lru"""
    cache = LRUCache(3000)

    rectangle_1 = Rectangle(1, 1, "red")
    rectangle_2 = RectangleSlot(1, 1, "blue")

    ref_a = weakref.ref(rectangle_1)

    lst_1 = [rectangle_1 for i in range(1000)]
    lst_2 = [rectangle_2 for i in range(1000)]

    for i, j in enumerate(lst_1):
        cache.set("k {0}".format(i), j)

    for i, j in enumerate(lst_2):
        cache.set("k {0}".format(1000 + i), j)

    for i in range(1000):
        cache.set("k {0}".format(2000 + i), ref_a)


@profile
def profile_func():
    """profiling function"""
    time.sleep(0.5)
    make_cache()


def main():
    """main function"""
    profiler = cProfile.Profile()
    profiler.enable()
    profile_func()
    profiler.disable()
    profiler.print_stats()


if __name__ == "__main__":
    main()
