# 2. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.    
# *Примеры:*
#   - 6,78 -> 7
#    - 5 -> нет
#    - 0,34 -> 3

print('Введите дробь: ')
drob = float(input())
drob = int((drob % 1) * 10)
# drob = int((drob * 10) % 10)
print(drob)