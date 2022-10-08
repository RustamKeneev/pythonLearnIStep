# for number in range(1, 10):
#     print(number)


class MyRange:
    def __init__(self, start, end):
        self.startsss = start
        self.endssss= end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.endssss:
            number = self.current
            self.current += 1
            return number
        raise StopIteration


first_range = MyRange(20, 30)
# print(first_range)
iter(first_range)
for number in first_range:
    print(number)


