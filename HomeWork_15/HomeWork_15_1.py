class reverse_iterator:
    def __init__(self):
        self.data = None
        self.size = None
        self.index = None

    def __init__(self, sq: list) -> None:
        self.data = sq[::-1]
        self.size = len(sq)
        self.index = -1

    def __next__(self):
        if self.index < self.size - 1:
            self.index += 1
            return self.data[self.index]
        else:
            raise StopIteration

    def __iter__(self):
        self.index = -1
        return self


def rev_iterator(source: list) -> iter:
    return iter(source[::-1])


it = reverse_iterator([1, 2, 3, 4, 5])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
