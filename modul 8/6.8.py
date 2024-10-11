class IntDataFrame:
    def __init__(self, numbers):
        self.column = [int(x) for x in numbers]
    def count(self):
        return sum([1 for x in self.column if x != 0])
    def unique(self):
        return len(set(self.column))
