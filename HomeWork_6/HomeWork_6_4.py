text = input('Enter some text:')
n = ''
for i in text:
    if i.isalpha():
        n = ''.join([n,i])
print('Correct text is:', str(n))