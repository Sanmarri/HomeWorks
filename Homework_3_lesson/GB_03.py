"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""

def my_func(x, y, z):
    if x >= y and z >= y:
        return x + z
    elif y >= x and z >= x:
        return y + z
    elif x >= y >= z:
        return x + y
    elif y >= x >= z:
        return x + y

print(my_func(2,2,2))
