def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg: list):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

double(10)
double(10.5)
double('hello')

numbers = [10,20,30]
change(numbers)