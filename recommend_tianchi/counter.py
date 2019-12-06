class Counter:
    def __init__(self, n, label=""):
        self.c = 0
        self.n = n
        self.label = label
        self.next_milestone = n / 100

    def count_print(self):
        self.c += 1
        if self.c >= self.next_milestone:
            print("%s:\t%.2f%%" % (self.label, self.c * 100 / self.n))
            self.next_milestone += self.n / 100
