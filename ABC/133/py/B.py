n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        dist = 0
        for s in range(d):
            dist += pow(abs(x[i][s] - x[j][s]), 2)
        dist = pow(dist, 1/2)
        if dist.is_integer():
            ans+=1
print(ans)
