n,m = map(int, input().split())
a = list(map(int, input().split()))
ans = n-sum(a)

if ans >= 0:
    print(ans)
else:
    print(-1)
