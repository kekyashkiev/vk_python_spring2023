from unittest import mock
from unittest.mock import patch
import unittest
import parse_json


class TestParse(unittest.TestCase):
    def setUp(self) -> None:
        self.data = """{ "name": "Ilya Dmitriy Roman Petr",
                        "surname":"Kekyashkiev Gusev Loos Lenskiy",
                        "age":"20 21 22 23",
                        "faculty":"physical chemical biological historical"}"""

    def test_parse_1(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj, ["name"], [])
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual([], mock_obj.mock_calls)

    def test_parse_2(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj,
                                  ["name"], ["Ilya", "Roman"])
            self.assertEqual(mock_obj.call_count, 2)
            self.assertEqual([mock.call("name", "Ilya"),
                              mock.call("name", "Roman")], mock_obj.mock_calls)

    def test_parse_3(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj, [""])
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual([], mock_obj.mock_calls)

    def test_parse_4(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj, ["faculty", "name"],
                                  ["21", "physical", "Ilya"])
            self.assertEqual(mock_obj.call_count, 2)
            expected_calls = [
                mock.call("faculty", "physical"),
                mock.call("name", "Ilya"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

    def test_parse_5(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj)
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual(mock.call(), mock_obj.mock_calls)

    def test_parse_6(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj, ["name", "age"], ["28"])
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual(mock.call(), mock_obj.mock_calls)

    def test_parse_7(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj,
                                  ["name", "age"],
                                  ["Roman", "Petya", "Vlad", "Evgeniy", "Igor"]
                                  )
            self.assertEqual(mock_obj.call_count, 1)
            expected_calls = [
                mock.call("name", "Roman")
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

    def test_parse_9(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data, mock_obj, ["room"])
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual(mock.call(), mock_obj.mock_calls)

    def test_parse_11(self):
        with patch("parse_json.word_handler") as mock_obj:
            parse_json.parse_json(self.data)
            self.assertEqual(mock_obj.call_count, 0)
            self.assertEqual(mock.call(), mock_obj.mock_calls)


if __name__ == '__main__':
    unittest.main()
