# Написать программу, которая генерирует случайное трехзначное число и вычисляет сумму его цифр.

from random import randint

# РЕШЕНИЕ 1

n = randint(100, 999)

print(f"Случайное число: {n}")

d1 = n // 100
# print(d1)

d2 = (n % 100) // 10
# print(d2)

d3 = n % 10
# print(d3)

sum1 = d1 + d2 + d3
print(f'Сумма его цифр: {sum1}')

# РЕШЕНИЕ 2

c = str(n)

c1 = int(c[0])
# print(c1)

c2 = int(c[1])
# print(c2)

c3 = int(c[2])
# print(c3)

sum2 = c1 + c2 + c3
print(f'Сумма его цифр: {sum2}')