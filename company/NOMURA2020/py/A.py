h1, m1, h2, m2, k = map(int, input().split())

ans = (h2 - h1)*60 + (m2-m1)
if (ans - k)>=0:
    print(ans - k)
else:
    print(0)
