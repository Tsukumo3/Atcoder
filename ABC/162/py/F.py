n = int(input())
a = list(map(int, input().split()))

w = n//2
inf = -1*(pow(10,9)+7)
dp0 = [inf]*n
dp1 = [inf]*n

dp0[0], dp0[1] = a[0], a[1]
dp1[0], dp1[1] = a[0], a[0]+a[1]

for i in range(1,n-1):
    dp0[i+1] = max(a[i+1], dp0[i])
    dp1[i+1] = max()


print(*dp, sep="\n")
