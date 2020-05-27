n , l = map(int, input().split())
x = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [0 for i in range(l+2)]
dp[1] = t[0]

for i in x:
    dp[i] += t[2]

for i in range(2,4):
    dp[i] = min(
                dp[i] + dp[i-1] + t[0],
                dp[i] + dp[i-2] + t[1] + t[0],
            )

for i in range(4, l+1):
    dp[i] = min(
                dp[i] + dp[i-1] + t[0],
                dp[i] + dp[i-2] + t[1] + t[0],
                dp[i] + dp[i-4] + t[1]*3 + t[0]
            )
print(dp[l])
