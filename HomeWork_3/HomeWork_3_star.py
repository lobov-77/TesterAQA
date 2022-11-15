number = int(input('Введите трехзначное число:'))

reversed_number = 0

while number > 0:
    last_number = number % 10
    reversed_number = (reversed_number * 10) + last_number
    number = number // 10

print(f'Reserved number is: {reversed_number}')
