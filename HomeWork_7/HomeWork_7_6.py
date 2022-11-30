A = []
N = int(input('Enter a digit: '))
for num in range(N):
    x = int(input('Enter a numer: '))
    A.append(x)
max = A[0]
min = A[0]
for i in range(0,len(A)):
    if A[i] > max:
        max = A[i]
for i in range(0,len(A)):
    if A[i] < min:
        min = A[i]
print(f'This is max: {max} and this is min:{min}')
