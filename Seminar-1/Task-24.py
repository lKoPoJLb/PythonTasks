L = int(input("Введите длину окружности. L = "))
p = 3.14

R = round(L / (2 * p), 3)
S = round(p * pow(R, 2), 3)

print(f'R = {R}\nS = {S}')