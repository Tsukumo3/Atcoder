"""
f(n) , f(n+1)の値を求める
f(3456)を求める時

f(0) = 0, f(1) = 1 とする

f(3) = min
(
    f(0) + 3
    f(1) + 7
)
f(4) = min
(
    f(0) + 4
    f(1) + 6
)

f(34) = min
(
    f(3) + 4
    f(4) + 6
)
f(35) = min
(
    f(3) + 5
    f(4) + 5
)

f(345) = min
(
    f(34) + 5
    f(35) + 5
)
f(346) = min
(
    f(34) + 4
    f(35) + 6
)
f(3456) = min
(
    f(345) + 6
    f(346) + 4
)
"""
N = input()
n = [int(i) for i in N]

f0 = 0
f1 = 1

dp = f0, f1

# 桁DP
for i in n:
    # 支払い枚数を考える
    fn_0 = min(dp[0] + i, dp[1] + 10 - i)
    fn_1 = min(dp[0] + (i+1), dp[1] + 10 - (i+1))
    dp = fn_0, fn_1

print(dp[0])
