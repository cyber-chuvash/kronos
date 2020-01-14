import re

from kronos import time_intervals


_time_intervals = {
    r'sec': time_intervals.Seconds,
    r'min': time_intervals.Minutes,
    r'h': time_intervals.Hours,
    r'd': time_intervals.Days,
    r'w': time_intervals.Weeks,
    r'M': time_intervals.Months,
    r'y': time_intervals.Years,
}

_time_int_regex = {}

for _name, _interval in _time_intervals.items():
    _time_int_regex[re.compile(r'(\d+)\s+' + _name)] = _interval


def parse(string):
    result_seconds = 0

    for regex, interval_class in _time_int_regex.items():
        for match in regex.finditer(string):
            num = int(match.group(1))
            result_seconds += interval_class(num).get_seconds()

    return result_seconds

