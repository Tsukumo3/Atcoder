m, d = map(int, input().split())
ans = 0
for i in range(2, m+1):
    for j in range(20, d+1):
        s = str(j)
        d10 = int(s[0])
        d1 = int(s[1])
        if d1 == 1 or d10 == 1:
            continue
        elif i == d1 * d10:
            #print(i,d10,d1)
            ans += 1
print(ans)
