"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

x = int(input())
y = int(input())

def division(x, y):
    if x != 0 and y != 0:
        return x / y
    elif y == 0:
        return "It's a mistake!"
    elif x == 0:
        return 0

print(division(x, y))
