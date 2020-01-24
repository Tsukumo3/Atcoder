N,K,M = map(int, input().split())
A_n1 = list(map(int, input().split()))

import math

ans = 0
nokori = M*N - sum(A_n1)
#print(nokori)

if nokori <= 0:
    print(0)
elif nokori > K:
    print(-1)
else:
    print(nokori)
