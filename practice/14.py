# 14. Создайте массив, содержащий 10 первых нечетных чисел. Выведете элементы массива на консоль в одну строку, разделяя запятой.

odd_numbers = [2 * i + 1 for i in range(10)]


str_numbers = [str(num) for num in odd_numbers]


result_string = ", ".join(str_numbers)

print(result_string)
