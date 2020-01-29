import re

from kronos import time_intervals
from kronos.language import english


class Parser:
    def __init__(self, langs=None):
        # English language as the default
        if langs is None:
            langs = [english]

        elif not isinstance(langs, (list, set, tuple)):
            langs = [langs]

        self._time_interval_regex = {}

        for lang in langs:
            for name, interval in lang.interval_names.items():
                regex = re.compile(rf'(?a:(\d+))\s*{name}\b', flags=re.IGNORECASE)
                self._time_interval_regex[regex] = interval

    def parse(self, string):
        result_seconds = 0
        match = None

        for regex, interval_class in self._time_interval_regex.items():
            for match in regex.finditer(string):
                num = int(match.group(1))
                result_seconds += interval_class(num).get_seconds()

        return result_seconds if match else None


_default_parser = Parser()


def parse(string, langs=None):
    if langs is None:
        return _default_parser.parse(string)
    else:
        return Parser(langs=langs).parse(string)
