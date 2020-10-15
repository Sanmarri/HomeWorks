"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

with open("seventh_text.txt") as seven_task:
    list_firm = []
    dict_firm = {}
    dict_average = {}
    average = 0

    for line in seven_task:
        firm = line.split()
        profit = int(firm[2]) - int(firm[3])
        dict_firm[firm[0]] = profit
        if profit > 0:
            average += profit

    dict_average['average_profit'] = round(average / len(dict_firm))

    list_firm.append(dict_firm)
    list_firm.append(dict_average)

with open("seventh_text.json", "w") as seven_task_result:
    json.dump(list_firm, seven_task_result)

