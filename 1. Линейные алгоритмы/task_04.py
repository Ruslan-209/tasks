# С клавиатуры вводятся границы числового диапазона. 
# Получите случайное целое число в его пределах и выведите его на экран.

from random import randrange, randint

number1 = int(input('Введите нижнюю границу: '))
number2 = int(input('Введите верхнюю границу: '))

result = randint(number1, number2)

print(result)

# чтобы верхняя граница не входила

n = randrange(number1, number2)
print(n)
