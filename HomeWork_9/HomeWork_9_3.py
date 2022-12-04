A = []
N = int(input('Enter a digit: '))
for num in range(N):
    x = int(input('Enter a numer: '))
    A.append(x)
B = str(A).replace(',', ' ')
file = open('numbers.txt', 'w')
file.write(B)
file.close()
