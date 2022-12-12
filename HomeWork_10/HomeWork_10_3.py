def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))


print(sum_range(start=int(input('Enter start number: ')), end=int(input('Enter end number: '))))
