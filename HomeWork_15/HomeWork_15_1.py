def reverse_iterator(source: list) -> iter:
    return iter(source[::-1])


it = reverse_iterator([1, 2, 3, 4, 5])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
