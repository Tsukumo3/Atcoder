n, k = map(int, input().split())
mod = pow(10, 9) + 7
ans = 0
for i in range(k, n+2):
    #小さい方からi個選ぶ
    mini = i*(i-1)//2
    maxa = (2*n-i+1)*i//2
    ans = (ans + (maxa - mini + 1)% mod)% mod
print(ans)
