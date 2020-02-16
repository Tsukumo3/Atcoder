n = int(input())
h = list(map(int,input().split()))

'''
n番目の場所に到達する時
n-1番目から、1つ飛んでくる
n-2番目から、２つ飛んでくる
可能性がある　その時の最小値を考える

初期条件
dp[0] = 0
dp[1] = h[1] - h[0]

*** n-1
dp[n] = dp[n-1] + abs(h[n] - h[n-1])

*** n-2
dp[n] = dp[n-2] + abs(h[n] - h[n-2])

漸化式
n >= 2
dp[n] = min(dp[n-1] + abs(h[n] - h[n-1]) , dp[n-2] + abs(h[n] - h[n-2]))

'''

def choice_min(n0, n1):
    if n0 <= n1:
        return n0
    else:
        return n1


dp = [0, abs(h[1] - h[0])]

for i in range(2,n):
    dp.append(
        choice_min(
            dp[i-1] + abs(h[i] - h[i-1]),
            dp[i-2] + abs(h[i] - h[i-2])
        )
    )

#print(dp)
print(dp[n-1])
