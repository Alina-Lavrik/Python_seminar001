# 3. Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно ((5 и 10) или 15), но не 30.
# 20 -> ok

print('Введите число от 1 до 200: ')
A = float(input())

'''if A % 30 == 0:
    print('No')
elif A % 5 == 0 and A % 10 == 0:
    print('Ok')
elif A % 15 == 0:
    print('Ok')
else: 
    print('Число не кратно 5') '''

if (A % 5 == 0 and A % 10 == 0 or A % 15 == 0) and A % 30 != 0:
    print('Yes')
else:
    print('No')
    