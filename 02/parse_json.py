"""Функция, которая в качестве аргументов принимает строку json,
список полей, которые необходимо обработать, список имён, которые нужно найти
и функцию-обработчика имени, который срабатывает,
когда в каком-либо поле было найдено ключевое имя."""


import json


def word_handler(field, word):
    pass


def parse_json(json_str: str, word_handler=None,
               required_fields=None, keywords=None):

    json_dict = json.loads(json_str)

    if required_fields is None or keywords is None or word_handler is None:
        return

    for field in required_fields:
        if field in json_dict:
            words = json_dict[field].split()
            for word in keywords:
                if word in words:
                    word_handler(field, word)
