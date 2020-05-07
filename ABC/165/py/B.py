import math
c = 100
x = int(input())
ans = 0
while(True):
    ans += 1
    c = c*1.01
    c = math.floor(c)
    if x <= c:
        break
print(ans)
