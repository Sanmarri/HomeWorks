"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

second_task = open("second_text.txt")
lines = 0
quantity_words = []
for line in second_task:
    lines += 1
    words = line.split()
    quantity_words.append(len(words))


print(lines)
print(quantity_words)

print(f'В файле {lines} строк')
print('Какая строка тебя интересует?')

answer = int(input())

if 0 < answer <= lines:
    print(f'В {answer} строке {quantity_words[answer-1]} строк')
else:
    print(f'Ну что с тобой, котик? Я же сказала, что в файле {lines} строк!')