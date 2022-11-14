
number = int(input('введите трехзначное число:'))

c = number % 10
number = number // 10
b = number % 10
a = number // 10

reversed_number = (c, b, a)
print(f'reserved number is: {reversed_number}')