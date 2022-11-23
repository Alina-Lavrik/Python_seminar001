# Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них

# max = int(input())   # a

# for i in range(4):
#     b = int(input())
#     if b > max:
#        max = b
# print(max)


a = list(map(int, input().split()))  # map переводит введенные значения в int
print(max(a))
