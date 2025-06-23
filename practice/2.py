# 2. Из трех данных чисел выбрать наименьшее и наибольшее

input_str = input("Введите три числа через пробел: ")
numbers_str = input_str.split()
numbers = [float(n) for n in numbers_str]

smallest = min(numbers)
largest = max(numbers)

print(f"Из чисел {numbers}:")
print(f"Наименьшее: {smallest}")
print(f"Наибольшее: {largest}")
