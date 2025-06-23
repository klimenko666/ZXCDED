# 17. Построить строку, состоящую из малых букв латинского алфавита (по алфавиту).


import string


alphabet_string = string.ascii_lowercase

print("Способ 1 (модуль string):")
print(alphabet_string)


print("\nСпособ 2 (через chr и ord):")
alphabet_list = []
for i in range(26):
    char_code = ord('a') + i
    alphabet_list.append(chr(char_code))

manual_alphabet_string = "".join(alphabet_list)
print(manual_alphabet_string)
