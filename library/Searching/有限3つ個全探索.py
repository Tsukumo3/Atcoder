n, y = map(int, input().split())

for i in range(n+1):
    m = n - i# 残り
    for j in range(m+1):
        k = m - j
        price = i*10000 + j*5000 + k*1000
        if y == price:
            print(i, j, k)
            exit()
else:
    print(-1,-1,-1)
