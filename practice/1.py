# 1. Даны три целых числа. Возвести в квадрат отрицательные числа и в третью степень — положительные (число 0 не изменять).

input_str = input("Введите три целых числа через пробел: ")
numbers_str = input_str.split()
numbers = [int(n) for n in numbers_str]

result_numbers = []

for num in numbers:
    if num < 0:

        result_numbers.append(num ** 2)
    elif num > 0:

        result_numbers.append(num ** 3)
    else:

        result_numbers.append(num)

print("Исходные числа:", numbers)
print("Преобразованные числа:", result_numbers)