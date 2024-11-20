class sequence_repeat:
    def __init__(self, sequence , number):
        self.sequence = sequence
        self.number = number
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            inx = self.counter % len(self.sequence)
            self.counter += 1
            return self.sequence[inx]
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
