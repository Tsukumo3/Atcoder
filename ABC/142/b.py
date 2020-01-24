n,k = map(int, input().split())

kids = list(map(int, input().split()))

ans = 0

for kid in kids:
    if kid >= k:
        ans += 1

print(ans)
