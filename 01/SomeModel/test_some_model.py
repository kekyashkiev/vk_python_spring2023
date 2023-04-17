from unittest.mock import patch
from unittest import mock
import unittest
import some_model


class TestSomeModel(unittest.TestCase):
    def setUp(self):
        self.var_of_class = some_model.SomeModel()
        self.text = "hello, world"

    def test_some_model(self):
        with patch("some_model.SomeModel.predict") as mock_var:
            self.assertEqual(type(self.text), str)
            mock_var.side_effect = [0.1, 0.90, 0.7, 0, 0.45, 0.99,
                                    0.76, 0.456, 0.1, 0.28]
            arr = [
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class, 0.7),
                    'неуд'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class, 0.7),
                    'отл'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class, 0.7),
                    'норм'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class,
                        good_thresholds=0.7),
                    'неуд'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class,
                        good_thresholds=0.7),
                    'норм'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class,
                        good_thresholds=0.7),
                    'отл'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class,
                        good_thresholds=0.7),
                    'отл'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class,
                        good_thresholds=0.7),
                    'норм'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class, bad_thresholds=0.05,
                        good_thresholds=0.7),
                    'норм'),
                (
                    some_model.predict_message_mood(
                        self.text, self.var_of_class, 0.25, 0.89),
                    'норм'),
            ]

            for i in range(len(arr)):
                self.assertEqual(arr[i][0], arr[i][1])

            self.assertEqual([mock.call('hello, world')] * 10,
                             mock_var.mock_calls)


if __name__ == '__main__':
    unittest.main()
