A = []
N = int(input('Enter a digit: '))
for num in range(N):
    x = int(input('Enter a numer: '))
    A.append(x)
B = str(A).replace(',', ' ')
C = B.replace(']', ' ')
D = C.replace('[', ' ')
file = open('numbers.txt', 'w')
file.writelines(D)
file.close()
