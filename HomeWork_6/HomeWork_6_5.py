email = input('Enter your email, please:')
if '@' and '.' not in email :
    print('No')
elif '@' and '.' in email:
    print('Yes')
else:
    print('Try again')
