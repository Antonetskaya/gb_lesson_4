# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random
from functools import reduce
spisok = [random.randint(100, 1000) for el in range(4)]
print(spisok)
print(reduce(lambda x, y: x * y, spisok))
