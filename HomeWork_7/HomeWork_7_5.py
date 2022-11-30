A = []
C = []
try:
    for num in range(5):
        x = int(input('Enter a numer: '))
        A.append(x)
        if x > 5:
            C.append(x)
    print(C)
except Exception as e:
        print('Enter a digit please')

