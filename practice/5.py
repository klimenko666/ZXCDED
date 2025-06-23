# 5. Найти периметр и площадь прямоугольного треугольника, если даны длины его катетов a и b. 


import math

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

area = (a * b) / 2

hypotenuse = math.sqrt(a**2 + b**2)

perimeter = a + b + hypotenuse

print(f"Площадь треугольника: {area:.2f}")
print(f"Периметр треугольника: {perimeter:.2f}")