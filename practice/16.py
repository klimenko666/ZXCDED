# 16. Дана строка S и число N. Преобразовать строку S в строку длины N следующим образом: если длина строки S больше N, то отбросить первые символы, если длина строки S меньше N, то в ее начало добавить символы "." (точка). 

def transform_string(s, n):
    """Преобразует строку s в строку длины n."""
    len_s = len(s)

    if len_s > n:

        return s[-n:]
    elif len_s < n:

        return s.rjust(n, '.')
    else:

        return s


s1 = "Programming"
n1 = 7
print(f"'{s1}' (len={len(s1)}) -> {n1} = '{transform_string(s1, n1)}'")

s2 = "Python"
n2 = 10
print(f"'{s2}' (len={len(s2)}) -> {n2} = '{transform_string(s2, n2)}'")

s3 = "Test"
n3 = 4
print(f"'{s3}' (len={len(s3)}) -> {n3} = '{transform_string(s3, n3)}'")
