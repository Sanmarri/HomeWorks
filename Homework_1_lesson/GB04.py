# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = input()
i = 0
x = 0

while i < len(number):
    if x < int(number[i]):
        x = int(number[i])
    i += 1

print(x)
