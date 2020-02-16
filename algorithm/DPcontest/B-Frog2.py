n, k = map(int, input().split())
h = list(map(int,input().split()))

if k > n:
    k = n-1

'''
n番目の場所に到達する時
n-1番目から、1つ飛んでくる
n-2番目から、２つ飛んでくる
...
n-K番目から、kつ飛んでくる

可能性がある　その時の最小値を考える

初期条件
dp[0] = 0
dp[1~Kまで]を計算

*** n-j
dp[n] = dp[n-j] + abs(h[n] - h[n-j])

漸化式
n >= 2
dp[n] = min(jump_list)

1~K
jump_list = [1 ~ j で dp[n] = dp[n-j] + abs(h[n] - h[n-j])]

k~N
jump_list = [1 ~ k で dp[n] = dp[n-j] + abs(h[n] - h[n-j])]

'''

#初期値
dp = [0]

def create_jump_list(j,i):
    alist = []
    for x in range(j, i):
        alist.append(
            dp[x] + abs(h[i] - h[x])
        )
    return alist

# kまで
for i in range(1, k+1):
    jump_list = create_jump_list(0,i)
    dp.append(
        min(jump_list)
    )

for i in range(k+1,n):
    jump_list = create_jump_list(i-k, i)
    dp.append(
        min(jump_list)
    )

print(dp)
print(dp[n-1])
