from kronos import time_intervals

interval_names = {
    r's(ec(ond)?)?s?': time_intervals.Seconds,
    r'(?-i:m)|min(ute)?s?': time_intervals.Minutes,
    r'h(our)?s?': time_intervals.Hours,
    r'd(ay)?s?': time_intervals.Days,
    r'w(eek)?s?': time_intervals.Weeks,
    r'(?-i:M)|mon(th)?s?': time_intervals.Months,
    r'y(ear)?s?': time_intervals.Years,
}
