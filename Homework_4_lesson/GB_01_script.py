"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

sotrudnik, hours, rate, prize = argv[1:]

print("Worker: ", sotrudnik)
print("Hours: ", hours)
print("Rate:", rate)
print("Prize: ", prize)