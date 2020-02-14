'''
問題 2:　ナップサック問題

nn 個の品物があり、ii 番目の品物のそれぞれ重さと価値が weight[i],value[i]weight[i],value[i] となっている (i=0,1,...,n−1i=0,1,...,n−1)。
これらの品物から重さの総和が WW を超えないように選んだときの、価値の総和の最大値を求めよ。

【制約】
・1≤n≤100
・weight[i],value[i] は整数
・1≤weight[i],value[i]≤1000
・1≤W≤10000

【数値例】
1)
　n=6, W=9
　(weight,value)=(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)
　
　答え: 94 ((3,6), (1,3), (5,85) を選んだときが最大です)
'''

def choice_max(n0, n1):
    if n0 >= n1:
        return n0
    else:
        return n1

def solve(n, w, a):

    #初期値
    dp = [[0 for _ in range(w)]]
    print(dp)

    #dp遷移
    '''
    dp遷移
    数字を足したことで増えるなら助し、たさないほうが高い時はたさない
    dp[i+1] = dp[i] + a[i] | dp[i]
    '''
    for i in range(n):
        for j in range(w):
            dp.append(choice_max(dp[i] + a[i], dp[i]))

    #DP table
    print(dp)
    #answer
    print(dp[n])

if __name__ == '__main__':
    n = 6
    w = 9
    a = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]

    solve(n, w, a)
