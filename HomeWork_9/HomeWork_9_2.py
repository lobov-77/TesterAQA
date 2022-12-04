file = open('data.txt', 'w')
text = input('Enter some text: ')
file.writelines(text)
file.close()
