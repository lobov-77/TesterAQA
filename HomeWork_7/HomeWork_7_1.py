n = []
try:
    first = int(input('Enter first number:'))
    second = int(input('Enter second numbe:'))
    third = int(input('Enter third number:'))
    fouth = int(input('Enter fouth number:'))
    fivth = int(input('Enter fivth number:'))
    n = [first, second, third, fouth, fivth]
    print(n)
except Exception as e:
    print('Enter a digit please')