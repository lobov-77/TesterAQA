n = int(input('Enter numbers of stars:'))
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)
