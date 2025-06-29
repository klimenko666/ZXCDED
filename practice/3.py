# 3. Ввести с клавиатуры два числа. Определить, что больше, сумма квадратов или квадрат суммы этих чисел. Ответ вывести в виде сообщения.

a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))

sum_of_squares = a**2 + b**2

square_of_sum = (a + b)**2

print(f"Сумма квадратов ({a}² + {b}²) = {sum_of_squares}")
print(f"Квадрат суммы (({a} + {b})²) = {square_of_sum}")

if sum_of_squares > square_of_sum:
    print("Сообщение: Сумма квадратов больше квадрата суммы.")
elif square_of_sum > sum_of_squares:
    print("Сообщение: Квадрат суммы больше суммы квадратов.")
else:
    print("Сообщение: Сумма квадратов равна квадрату суммы.")