import random

file = open('random_numbers.txt', 'w')
random_number = [random.randint(0, 1000) for _ in range(100)]

fs = [int(x) for x in random_number]
x = str(fs)
for x in fs:
    file.write(str(x) + '\n')
