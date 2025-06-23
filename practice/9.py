# 9. В заданной строке посчитать количество русских букв «А».

input_string = "Ах, какая прекрасная Астра! Аппетит разыгрался."

count_lower_a = input_string.count('а')
count_upper_a = input_string.count('А')

total_count = count_lower_a + count_upper_a

print(f"Исходная строка: '{input_string}'")
print(f"Количество букв 'а': {count_lower_a}")
print(f"Количество букв 'А': {count_upper_a}")
print(f"Общее количество букв 'а'/'А': {total_count}")
