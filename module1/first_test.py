number = 10
def spam(number):
  return 'bulochka'*number
print(spam(number))
'''
Function should return something like this:
spam(1);#bulochka
spam(3);#bulochkabulochkabulochka
But it is broken. Fix it please!

Эта функция принимает числовой параметр. Должна вернуть строку, которая
повторяется столько раз, сколько параметров передано. Она уже написана,
но не работает. Любым способом заставьте ее работать.
'''


list_of_numbers = [23, 5, 33, 2, 10]
def my_sum(list_of_numbers):
  a = 0
  for i in list_of_numbers:
    if type(i) == int:
      a += i
  return a
print(my_sum(list_of_numbers))
pass

"""
Function receives a list with integer numbers,
should return its sum as an integer. Do not use built in summarize functions.
:param list
Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
Не использовать встроенные функции суммирования.
"""
pass
    #  ...wite your code here

string = ('happy my day for a one list septetw sdfsdfsdfsdf fdsfsdfdsfsferw')
def shortener(string):
  w = []
  for i in string.split():
    if len(i) > 6:
      i = i[:6] + '*'
      w.append(i)
    else:
      w.append(i)
  return ' '.join(w)


'''Function receives a long string with many words.
It should return the same string, but words,
larger then 6 symbols should be changed, symbols
after the sixth one should be replaced by symbol *
:param string
:returns string
Функция получает на вход длинную строку с множеством слов.
Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
функция должна вместо всех символов после шестого поставить одну звездочку.
Пример: Из слова 'verwijdering' должно получиться 'verwij* '''

    #  ...wite your code here

words = ('fdsfsdfsdfsdf', 'daddywayerd', 'hekk', 'loseel')
def compare_ends(words):
  spk = []
  j = 0  
  for i in words:
    if len(i) >= 2 and i[0] == i[-1]:
      spk.append(i)
      j += 1
  return j
'''
Function receives an array of strings.
Please return number of strings, which
length is at least 2 symbols and first character
is equal to the last character

Функция получает на вход массив строк. Вернуть надо количество строк,
которые не короче двух символов и у которых первый и последний
символ совпадают.
'''
#  ...wite your code here