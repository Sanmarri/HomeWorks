# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

plus = int(input('Сколько ты заработал?'))
minus = int(input('А сколько потратил?'))

if plus > minus:
    print('Все в порядке, дом на Канарах уже близко')
    print(f'Ты заработал в {plus//minus} раз больше, чем вложил. Но это не предел!')
    shtat = int(input('Сколько, говоришь, у тебя сотрудников?'))
    print(f'Вот каждый из них принес {plus // shtat} бубликов. Сам реши, кого уволить')
elif minus > plus:
    print('Кажется, ты что-то делаешь не так. Попробуй начать заново')
else:
    print('Никакого результата. Оно тебе надо?')
