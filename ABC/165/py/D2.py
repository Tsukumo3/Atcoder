import math
a, b, n = map(int, input().split())
x = n

if b <= n:
    x = b-1

new = math.floor(a*x/b) - a * math.floor(x/b)
print(new)
