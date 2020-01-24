import math
H = int(input())
W = int(input())
N = int(input())

long = W

if H > W:
    long = H

ans = math.ceil(N/long)

print(ans)
