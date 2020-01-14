import re

from kronos import time_intervals
from kronos.language import english

_time_int_regex = {}

for _name, _interval in english.interval_names.items():
    _time_int_regex[re.compile(rf'(?a:(\d+))\s*{_name}\b', flags=re.IGNORECASE)] = _interval


def parse(string):
    result_seconds = 0
    match = None

    for regex, interval_class in _time_int_regex.items():
        for match in regex.finditer(string):
            num = int(match.group(1))
            result_seconds += interval_class(num).get_seconds()

    return result_seconds if match else None

