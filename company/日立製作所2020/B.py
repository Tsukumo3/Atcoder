A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = [list(map(int, input().split())) for i in range(M)]


min_price = min(a) + min(b)

#チケット処理
for i in range(M):
    low = a[t[i][0]-1] + b[t[i][1]-1] - t[i][2]
    if low < min_price:
        min_price = low
print(min_price)
