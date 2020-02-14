S,T = input().split()
A,B = map(int, input().split())
N = input()

if N == S:
    A -= 1
else:
    B -= 1

print(A,B)
