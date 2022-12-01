n = []
try:
    for num in range(5):
        x = int(input('Enter a numer: '))
        n.append(x)
    print(n)
except Exception as e:
    print('Enter a digit please')