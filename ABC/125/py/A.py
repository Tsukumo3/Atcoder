a, b, t = map(int, input().split())

now = a
cnt = 0
t += (0.5 - a)
while(t > 0):
    cnt += b
    now += a
    t -= a
print(cnt)
