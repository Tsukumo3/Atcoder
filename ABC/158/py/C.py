import math
a,b = map(int, input().split())

for i in range(1010):
    s = math.floor(i*0.08)
    t = math.floor(i*0.10)
    if s == a and t == b:
            print(i)
            break
else:
    print(-1)
