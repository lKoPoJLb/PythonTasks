import math

a, b = map(int, input("Введите неотрицательные числа: ").split())
Res = int(math.sqrt(a * b))

print(Res)