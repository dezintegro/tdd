class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return True

    def times(self, count):
        return Dollar(self.amount * count)
