# 10. В заданной строке удалить второй и четвертый по счету символы.

input_string = "Программирование"


if len(input_string) >= 4:
    result_string = input_string[:1] + input_string[2:3] + input_string[4:]
else:

    result_string = "Строка слишком короткая для этой операции"

print(f"Исходная строка: {input_string}")
print(f"Результат: {result_string}")
