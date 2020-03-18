n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    t = list(str(i))
    t = [int(i) for i in t]
    s = sum(t)
    if a <= s <= b:
        #print(t)
        ans += i
print(ans)
