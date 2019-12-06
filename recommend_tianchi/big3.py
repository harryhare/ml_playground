
class Big3:
    def __init__(self):
        self.one = 0.
        self.two = 0.
        self.three = 0.
        self.count = 0.

    def push(self, x):
        self.count += 1
        if x > self.one:
            self.three = self.two
            self.two = self.one
            self.one = x
        elif x > self.two:
            self.three = self.two
            self.two = x
        elif x > self.three:
            self.three = x

    def get_values(self):
        return self.one, self.two, self.three, self.count


