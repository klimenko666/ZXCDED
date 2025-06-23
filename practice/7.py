# 7. Даны натуральные числа х и у. Вычислить произведение , используя лишь операцию сложения. Задачу решить двумя способами x y

x = int(input("Введите первое натуральное число (x): "))
y = int(input("Введите второе натуральное число (y): "))


def multiply_with_loop(num1, num2):
    result = 0
    for _ in range(num2):
        result += num1
    return result


def multiply_with_recursion(num1, num2):

    if num2 == 0:
        return 0

    return num1 + multiply_with_recursion(num1, num2 - 1)


print(f"--- Результаты для {x} * {y} ---")
print(f"Способ 1 (цикл): {multiply_with_loop(x, y)}")
print(f"Способ 2 (рекурсия): {multiply_with_recursion(x, y)}")