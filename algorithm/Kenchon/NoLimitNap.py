def solve(N, W, ws, vs):
    dp = [0] * (W+1)
    for i in range(N):
        # 価値v, 重さw
        v = vs[i]; w = ws[i]
        for j in range(w, W+1):
            dp[j] = max(dp[j-w] + v, dp[j])
    return max(dp)
