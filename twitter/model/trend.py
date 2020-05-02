from json import JSONEncoder


class Trend(JSONEncoder):
    def __init__(self, name, volume="mock"):
        self.name = name if name is not None else ""
        self.volume = volume if volume is not None else 0

    def __str__(self):
        return "".join([self.name, ": ", str(self.volume)])

    def __eq__(self, other):
        return self.volume, self.name == other.volume, other._name

    def __lt__(self, other):
        return self.volume > other.volume


class Trends(JSONEncoder):
    def __init__(self, trends: list, location: str):
        self.trends = trends
        self.location = location

    def addTrend(self, trend: Trend):
        self.trends.append(trend)
