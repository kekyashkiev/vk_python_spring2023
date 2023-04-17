"""генератор для чтения и фильтрации файла"""


import re
import _io


def generator(file, arr):
    enter = set(map(lambda x: x.lower(), arr))
    if not isinstance(file, _io.TextIOWrapper):
        with open(file, "r", encoding='utf-8') as file_pointer:
            while True:
                line = file_pointer.readline()
                if not line:
                    break
                var = set(re.split(r'[ .!,:]', line.lower().rstrip()))
                if var.intersection(enter):
                    yield line.rstrip()
    else:
        while True:
            line = file.readline()
            if not line:
                break
            var = set(re.split(r'[ .!,]', line.lower().rstrip()))
            if var.intersection(enter):
                yield line.rstrip()
