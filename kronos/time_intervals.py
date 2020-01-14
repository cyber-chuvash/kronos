
class BaseTimeInterval:
    seconds = NotImplemented
    multiplier = NotImplemented

    def get_seconds(self):
        return self.seconds


class NaiveTimeInterval(BaseTimeInterval):
    def __init__(self, amount):
        self.seconds = amount * self.multiplier


class Seconds(NaiveTimeInterval):
    multiplier = 1


class Minutes(NaiveTimeInterval):
    multiplier = 60


class Hours(NaiveTimeInterval):
    multiplier = 3600


class Days(NaiveTimeInterval):
    multiplier = 86400


class Weeks(NaiveTimeInterval):
    multiplier = 604800


class Months(NaiveTimeInterval):
    # Naive implementation, to be improved TODO
    multiplier = 86400 * 30


class Years(NaiveTimeInterval):
    # Naive implementation, to be improved TODO
    multiplier = 86400 * 365
