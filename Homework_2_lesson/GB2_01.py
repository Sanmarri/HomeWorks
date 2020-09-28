# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = []

a = 1
b = 2.3
c = (4+5j)
d = 'python'
e = [1, 2, 3, 4, 5]
f = (13, 77)
g = set ('izmenenie')
h = {'jenih': 'Kolya', 'nevesta': 'Masha'}
i = True
j = False
k = bytearray(b"some text")
l = None

my_list.append(a)
my_list.append(b)
my_list.append(c)
my_list.append(d)
my_list.append(e)
my_list.append(f)
my_list.append(g)
my_list.append(h)
my_list.append(i)
my_list.append(j)
my_list.append(k)
my_list.append(l)

for m in my_list:
    print(type(m))
