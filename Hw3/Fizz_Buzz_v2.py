import sys
filename = sys.argv[1]
des = []
lel = ''
with open('numbers.txt', 'r') as filename:
    items = filename.readlines()
    for i in items:
        des.append([int(n) for n in i.split(',')])
for nums in des:   
    lel += '|'
    for num in range(1, nums[2]+1):
        if num % nums[2] and num % nums[1] == 0:
            lel += "FB" + " "
        elif num % nums[0] == 0:
            lel +="F" + " "
        elif num % nums[1] == 0:
            lel += "B" + " "
        else:
            lel += str(num) + " "
    lel += '|'
    lel += '\n'
with open('inject.txt', 'w') as file_vivod:
    file_vivod.write(str(lel))
    file_vivod.close()
    filename.close()
print('Выполнено! ' + '\n' + 'Вывод выполнен в новом файле: inject.txt :)')