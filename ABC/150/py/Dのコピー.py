from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

N ,M = map(int, input().split())
A_n = list(map(int,input().split()))
a_lcm = 1

for i in range(1,N):
    A_n[i] = A_n[i]//2
    a_lcm = lcm(a_lcm,A_n[i])

for A_i in A_n:
    if (a_lcm//A_i)%2 == 0:
        print(0)
        exit()

amari = M // a_lcm

if amari%2 == 1:
    amari = amari//2 + 1
else:
    amari = amari//2
print(amari)
