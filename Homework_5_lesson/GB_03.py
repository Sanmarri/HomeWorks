"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""

zarplata = open("third_text.txt")
workers = []
finances = []
sum_of_f = 0

for line in zarplata:
    info_line = line.split()
    workers.append(info_line[0])
    finances.append(int(info_line[1]))

print('Эти работники работают за копейки:')
for zp in range(len(finances)):
    sum_of_f += finances[zp]
    if finances[zp] < 20000:
        print(workers[zp])

print('Но в среднем зарплата на предприятии:')
print(sum_of_f / len(finances))

