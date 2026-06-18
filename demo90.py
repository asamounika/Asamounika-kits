pin=input('Enter the Password:')
try:
    if(pin=='1234'):
        print('Login is Successful')
    else:
        raise TypeError('Incorrect Password')
except TypeError as e:
    print(e)