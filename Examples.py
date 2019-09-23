#Пример №1
'''    x = int(input('Проверка четности числа, введдите число: \n'))
    if x % 2 == 0:
      print('Выбранное число четное!')
    elif x % 2 > 0:
      print('Выбранное число не четное!')
    else:
      print("Ошибка ввода")
    c = str(input('Очистить поле? Y/N? \n'))
    if c == "Y":
      print('\n' * 50)
    else:
      print('*•-.,_Ruddy_dev_,.-•* \n')'''
#Пример №2
'''rub = int(input('введите число   '))
if rub % 2 == 1 and not rub % 3 and not rub % 5 and rub % 10:
  print('Ваше число подходит.')
else:
  print('Ваше число не подходит.')'''
#Пример №3
'''x = int(input("Press Your number   "))
i = 1
while 1 <= x:
  if x % i == 0:
    print(i)
  i += 1
print([i for i in range(x) if not x % i])'''
#gel