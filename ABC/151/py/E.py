N,K = map(int,input().split())
A_n = list(map(int, input().split()))

div = 10**9+7
ans = 0

A_n.sort()

for i in range(N):
    ans += A_n[i] * (1*(i) + -1*(N-1-i))

print(ans%div)
