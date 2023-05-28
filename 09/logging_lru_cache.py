import sys
import logging
import logging.config
from collections import deque as cdeque


class CustomFilter(logging.Filter):
    def filter(self, record):
        return not len(record.msg.split()) % 2


log_config = {
    "version": 1,
    "handlers": {
        "file": {
            "filename": "cache.log",
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "output_file"},

        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "output_console"},

        "onlyfilter": {
            "filename": "cache.log",
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "output_file",
            "filters": ["filter"]},

        "consolewithfilter": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "output_console",
            "filters": ["filter"]},
    },

    "formatters": {
        "output_file": {
            "format": "%(levelname)s %(message)s"
        },
        "output_console": {
            "format": "%(levelname)s Gennadii, zdravstvui! - "
                      "console  %(message)s"
        }
    },

    "loggers": {
        "logfile": {
            "handlers": ["file"],
            "level": "DEBUG"
        },
        "logconsole": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        },
        "logfilter": {
            "handlers": ["onlyfilter"],
            "level": "DEBUG"
        },
        "logconsoleandfilter": {
            "handlers": ["consolewithfilter",
                         "onlyfilter"],
            "level": "DEBUG"
        }
    },

    "filters": {
        "filter": {
            "()": CustomFilter
        }
    }
}
logging.config.dictConfig(log_config)


class LRUCache:

    def __init__(self,  console, filtset, limit=4):
        if console and filtset:
            self.logger = logging.getLogger("logconsoleandfilter")
        elif console and not filtset:
            self.logger = logging.getLogger("logconsole")
        elif not console and filtset:
            self.logger = logging.getLogger("logfilter")
        else:
            self.logger = logging.getLogger("logfile")

        self.logger.info("initialization")

        self.limit = limit
        self.deque = cdeque(maxlen=limit)

    def set(self, key, value):
        if self.limit == 0:
            self.logger.info("method set, linit = 0")
            return
        keys_list = [key for key, value in self.deque]
        if key not in keys_list:
            self.logger.info("method set, "
                             "new key "
                             )
            self.deque.append((key, value))
            return True
        index = keys_list.index(key)
        self.logger.info("method set, existing key")
        old_key_and_val = self.deque[index]
        self.deque.remove(old_key_and_val)
        self.deque.append((key, value))
        return False

    def get(self, key):
        keys_list = [key for key, value in self.deque]
        if key in keys_list:
            self.logger.info("method get, key present")
            index = keys_list.index(key)
            key_and_val = self.deque[index]
            self.deque.remove(key_and_val)
            self.deque.append(key_and_val)
            return key_and_val[1]

        self.logger.info("method get, key missing")
        return None


if __name__ == "__main__":
    tmp = sys.argv
    consol = '-s' in tmp
    filt = '-f' in tmp
    d = LRUCache(consol, filt, 3)
    d.set('key_1', 'val_1')
    d.set('key_2', 'val_2')
    d.set('key_1', 'val_1')
    d.set('key_3', 'val_3')
    d.set('key_4', 'val_4')
    d.get('key_2')
    d.get('key_1')
