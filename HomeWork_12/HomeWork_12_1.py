def is_power_of_two():
    n = int(input('Enter a number: '))
    i = 1
    an = ''
    while i < n:
        i = i * 2
        if i == n:
            Response = 'YES'
        else:
            Response = 'NO'
    print(f'is_power_of_two ({n}) , "{Response}"')


is_power_of_two()
