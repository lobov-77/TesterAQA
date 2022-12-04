file = open('text_1.txt')
x = file.read()
y = x.split()
numbers = list(filter(str.isdigit, y))
print(numbers)






