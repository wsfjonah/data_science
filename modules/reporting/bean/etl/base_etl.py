class BaseETL:
    data = {}

    def __init__(self):
        pass

    def extract(self, key):
        pass

    def _parse_row(self, row):
        pass

    def store_value(self, key, value):
        if key in self.data:
            value = value + self.data[key]
        self.data[key] = value

    def to_chart_data(self):
        pass

    def draw(self):
        pass
