# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input())
hours = time // 3600
minutes = time % 3600 // 60
sec = time % 3600 % 60

print(hours)
print(minutes)
print(sec)

print(f'{hours:02}:{minutes:02}:{sec:02}')
