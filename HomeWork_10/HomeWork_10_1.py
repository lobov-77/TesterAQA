# def change_list():


def change_list():
    A = []
    N = int(input('Enter a digit: '))
    for num in range(N):
        x = int(input('Enter a numer: '))
        A.append(x)
    print(A[::-1])


change_list()
