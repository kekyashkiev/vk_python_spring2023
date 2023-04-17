import unittest
import _io
from file_generator import generator


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name = './text'

    def test_word(self):
        incom = {'Increase'}
        outcom = ['From fairest creatures we desire increase,']
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_few_words(self):
        incom = {'INcrease', 'diE'}
        outcom = ['From fairest creatures we desire increase,',
                  'That thereby beauty rose might never die,']
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_no_words(self):
        incom = {}
        outcom = []
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_wrong_word(self):
        incom = {'di'}
        outcom = []
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_two_wrong_words(self):
        incom = {'di', 'object'}
        outcom = []
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_one_correct_one_wrong(self):
        incom = {'inCrease', 'decision'}
        outcom = ['From fairest creatures we desire increase,']
        self.assertEqual(type(self.file_name), str)
        temp = generator(self.file_name, incom)
        self.assertEqual(list(temp), outcom)

    def test_file_word(self):
        incom = {'riPer'}
        outcom = ['But as the riper should by time decease,']
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)

    def test_file_few_words(self):
        incom = {'riPer', 'bear'}
        outcom = ['But as the riper should by time decease,',
                  'His tender heir might bear his memory:']
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)

    def test_file_no_words(self):
        incom = {}
        outcom = []
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)

    def test_file_wrong_word(self):
        incom = {'orchestra'}
        outcom = []
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)

    def test_file_correct_and_wrong_word(self):
        incom = {'bear', 'hello'}
        outcom = ['His tender heir might bear his memory:']
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)

    def test_file_two_wrong_words(self):
        incom = {'orchestra', 'unix'}
        outcom = []
        with open(self.file_name, 'r',  encoding="utf-8") as file:
            self.assertEqual(type(file), _io.TextIOWrapper)
            temp = generator(file, incom)
            self.assertEqual(list(temp), outcom)


if __name__ == '__main__':
    unittest.main()
