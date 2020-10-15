"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

numeral = open("fourth_text.txt")
rus_numeral = open("fourth_text_2.txt", 'w')

eng_num = numeral.readline().split()
eng_num [0] = 'Один'
rus_numeral.write((' ').join(eng_num) + '\n')

eng_num = numeral.readline().split()
eng_num [0] = 'Два'
rus_numeral.write((' ').join(eng_num) + '\n')

eng_num = numeral.readline().split()
eng_num [0] = 'Три'
rus_numeral.write((' ').join(eng_num) + '\n')

eng_num = numeral.readline().split()
eng_num [0] = 'Четыре'
rus_numeral.write((' ').join(eng_num) + '\n')