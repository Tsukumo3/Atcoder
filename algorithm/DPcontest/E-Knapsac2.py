n, w = map(int, input().split())
#0 weight , [1] value
table = [list(map(int, input().split())) for _ in range(n)]

'''
w = 10^5 -> 10^9
要素が多すぎる？
v = 10^9 -> 10^3
価値が減った？
なら価値を用いたDP作ろうよ！
'''

#print("お腹いっぱい")
dp = [[0] * (n+1) for i in range(n+1)]
def choice_max(a, b):
    if a > b:
        return a
    else:
        return b
for i in range(n):
    for j in range(w+1):
        if(j >= table[i][0]):
            dp[i+1][j] = choice_max(
                            dp[i][j],
                            dp[i][j - table[i][0]] + table[i][1]
                            )
        else:
            dp[i+1][j] = dp[i][j]
[print(item)for item in dp]
print(dp[n][w])
