text = input('Enter some text:')
if text.startswith('abc'):
    print(text.replace('abc', 'www', 1))
else:
    print(text + 'zzz')