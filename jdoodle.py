def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)

# Ввод чисел
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Вычисление НОД и коэффициентов x, y
gcd, x, y = extended_euclidean(a, b)

# Вывод результата
print(f"НОД: {gcd}")
print(f"x: {x}, y: {y}")