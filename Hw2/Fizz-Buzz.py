f = int(input('введите число fizz  '))
b = int(input('введите число buzz  '))
op = int(input('Введите число S   '))
for i in range(1, op):
    if i % f == 0 and i % b == 0:
        print('FB')
    elif i % f == 0:
        print('F')
    elif i % b == 0:
        print('B')
    else:
        print(i)
#be happy