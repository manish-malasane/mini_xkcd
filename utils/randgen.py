from random import randint


class NumGen:
    def __init__(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def __iter__(self):
        start = self.start
        end = self.end
        limit = self.limit
        while start <= limit:
            yield randint(start, end)
            start += 1
