"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("first_text.txt", "w") as first_task:
    phrase = input()
    first_task.write(phrase + '\n')
    while phrase != ' ':
        phrase = input()
        first_task.write(phrase + '\n')
