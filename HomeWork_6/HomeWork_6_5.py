email = input('Enter your email, please:')
if email.count('@') == 1 and email[0] != '@' and email.count('.') > 0 and email.rfind('.') > email.find('@'):
    print('Yes')
else:
    print('No')
