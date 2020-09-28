# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

year = {}

jfd = [1, 2, 12]
winter = dict.fromkeys(jfd, 'winter')

mam = [3, 4, 5]
spring = dict.fromkeys(mam, 'spring')

iia = [6, 7, 8]
summer = dict.fromkeys(iia, 'summer')

son = [9, 10, 11]
autumn = dict.fromkeys(son, 'autumn')

year.update(winter)
year.update(spring)
year.update(summer)
year.update(autumn)

print(year.get(8))

