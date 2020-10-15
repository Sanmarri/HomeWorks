"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open('fifth_text.txt', 'w') as numbers:
    number = list(input().split())
    numbers.write(' '.join(number))

with open('fifth_text.txt', 'r') as numbers:
    content = numbers.read().split()
    sum = 0

    for i in range(len(content)):
        sum += int(content[i])

print(sum)