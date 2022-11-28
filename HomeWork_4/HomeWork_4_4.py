n = int(input('Enter numbers of stars:'))
for i in range(0, n+1, +1):
    print(' ' * (n - i) + '*' * i)
