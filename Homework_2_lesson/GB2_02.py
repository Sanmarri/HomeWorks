# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

change_list = input().split()


for i in range(len(change_list)):
    if i % 2 != 0 and i != change_list[-1]:
        change_list[i], change_list[i - 1] = change_list[i - 1], change_list[i]

print(change_list)
