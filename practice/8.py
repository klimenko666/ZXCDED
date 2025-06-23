# 8.Даны два целых числа A и B (A < B). Вывести все целые числа, расположенные между данными числами (включая сами эти числа), в порядке их возрастания, а также количество N этих чисел. 
 
a = int(input("Введите число A: "))
b = int(input("Введите число B (A < B): "))

numbers_in_range = []

if a < b:

    for i in range(a, b + 1):
        numbers_in_range.append(i)
        print(i, end=" ")

    print()

    count = len(numbers_in_range)

    print(f"Количество чисел (N): {count}")
else:
    print("Ошибка: A должно быть меньше B.")
