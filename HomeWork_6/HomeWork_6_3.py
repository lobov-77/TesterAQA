text = input('Enter some text:')
if text.startswith('abc'):
    text_2 = text.replace('abc', 'www')
    print(text_2)
else:
    text_3 = text + 'zzz'
    print(text_3)
