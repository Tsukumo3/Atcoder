MOD = 10**9+7
n, m = map(int, input().split())
broken = [False for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
dp[0] = 1
for _ in range(m):
	broken[int(input())] = True
for i in range(1, n+1):
	if broken[i]:
		continue
	if i == 1:
		dp[i] = dp[i-1]
	else:
		dp[i] = dp[i-1] + dp[i-2]
		dp[i] %= MOD
print(dp[n])
