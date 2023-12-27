A = int(input()) #3
B = int(input()) #1
C = int(input()) #2

if A > B:
    if A > C:
        print(A)
    else:
        print(C)
elif B > A:
    if B > C:
        print(B)
    else:
        print(C)
elif C > A:
    if C > B:
        print(C)
    else:
        print(B)