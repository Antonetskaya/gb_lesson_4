# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Код в файле main.py (аргументы указывала в настройках этого файла, все работало)
from L4 import L4_zadacha_1
from sys import argv
file, vyrabotka, stavka, premiya = argv
print(L4_zadacha_1.zarplata(int(vyrabotka), int(stavka), int(premiya)))

# Код файла со скриптом в моем случае - L4_zadacha_1.py
def zarplata(vyrabotka, stavka, premiya):
    return vyrabotka * stavka + premiya



