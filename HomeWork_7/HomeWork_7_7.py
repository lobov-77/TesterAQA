text = input('Enter a text, please: ').split()
digits = list(filter(str.isdigit, text))
print(len(digits))


