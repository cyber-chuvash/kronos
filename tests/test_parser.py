import kronos


def test_simple_string():
    string = "1 sec"
    wanted_result = 1
    assert kronos.parse(string) == wanted_result


def test_simple_string_with_other_words():
    string = "That's just 1 sec. Is it enough?"
    wanted_result = 1
    assert kronos.parse(string) == wanted_result


def test_complex_string():
    string = "1 sec 2 min 34 h 1 w"
    wanted_result = 1 + 120 + (3600 * 34) + (86400 * 7)
    assert kronos.parse(string) == wanted_result


def test_repeated_intervals_string():
    string = "1 sec 4 sec 2 min 1 min 21 h 1 h"
    wanted_result = 1 + 4 + 120 + 60 + (3600 * 21) + 3600
    assert kronos.parse(string) == wanted_result


def test_empty_string():
    string = ""
    wanted_result = None
    assert kronos.parse(string) == wanted_result


def test_no_time_interval_string():
    string = "there's something in here. No time intervals though!"
    wanted_result = None
    assert kronos.parse(string) == wanted_result


def test_name_but_no_number_string():
    string = "Wait a sec, there is no time interval!"
    wanted_result = None
    assert kronos.parse(string) == wanted_result


def test_zero_seconds():
    string = "0 sec"
    wanted_result = 0
    assert kronos.parse(string) == wanted_result


def test_seconds():
    string = "12 sec"
    wanted_result = 12
    assert kronos.parse(string) == wanted_result


def test_minutes():
    string = "12 min"
    wanted_result = 60 * 12
    assert kronos.parse(string) == wanted_result


def test_hours():
    string = "12 h"
    wanted_result = 3600 * 12
    assert kronos.parse(string) == wanted_result


def test_days():
    string = "12 d"
    wanted_result = 86400 * 12
    assert kronos.parse(string) == wanted_result


def test_weeks():
    string = "12 w"
    wanted_result = 86400 * 7 * 12
    assert kronos.parse(string) == wanted_result


def test_month_naive():
    # Testing the naive implementation of 30-day months
    string = "12 M"
    wanted_result = 86400 * 30 * 12
    assert kronos.parse(string) == wanted_result


def test_years_naive():
    # Testing the naive implementation of 365-day years
    string = "12 y"
    wanted_result = 86400 * 365 * 12
    assert kronos.parse(string) == wanted_result
