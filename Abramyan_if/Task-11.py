A = int(input())
B = int(input())

if A == B:
    A += A
    B += B
else:
    A = 0
    B = 0

print(A, B)