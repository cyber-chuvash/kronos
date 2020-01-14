import re


_time_intervals = {
    r'sec': 1,
    r'min': 60,
    r'h': 3600,
    r'd': 86400,
    r'M': 2592000,
    r'y': 31536000
}

_time_int_regex = {}

for _name, _interval in _time_intervals.items():
    _time_int_regex[re.compile(r'(\d)+\s+' + _name)] = _interval


def parse(string):
    result_seconds = 0

    for regex, interval in _time_int_regex.items():
        for match in regex.finditer(string):
            num = int(match.group(1))
            result_seconds += num * interval

    return result_seconds

