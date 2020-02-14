'''
問題 1:　最大和問題

n 個の整数 a[0],a[1],…,a[n−1]が与えられる。
これらの整数から何個かの整数を選んで総和をとったときの、
総和の最大値を求めよ。また、何も選ばない場合の総和は 0 であるものとする。

【制約】
・1≤n≤100001≤n≤10000
・−1000≤a[i]≤1000

【数値例】
1)
　n=3
　a=(7,−6,9)
　答え: 16 (7 と 9 を選べばよいです)

2)
　n = 2
　a=(−9,−16)
　答え: 0 (何も選ばないのがよいです)
'''
def choice_max(n0, n1):
    if n0 >= n1:
        return n0
    else:
        return n1

def solve(n, a):

    #初期値
    dp = [0]

    #dp遷移
    '''
    dp遷移
    数字を足したことで増えるなら助し、たさないほうが高い時はたさない
    dp[i+1] = dp[i] + a[i] | dp[i]
    '''
    for i in range(n):
        dp.append(choice_max(dp[i] + a[i], dp[i]))

    #DP table
    print(dp)
    #answer
    print(dp[n])

if __name__ == '__main__':
    n = 3
    a = [7, -6, 9]
    solve(n, a)
