n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
#table A = 0, B = 1, C = 2
dp = [[0] * (3) for i in range(n+1)]

def choice_max(a, b):
    if a > b:
        return a
    else:
        return b


for i in range(n):
    for j in range(3):
        dp[i+1][j] = choice_max(
                        dp[i][(j+1)%3],
                        dp[i][(j+2)%3]
                        ) + cost[i][j]
#[print(i) for i in dp]
print(max(dp[n]))
