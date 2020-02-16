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
    dp = [[0 for _ in range(w+1)]]

    #dp遷移
    '''
    dp遷移
    数字を足したことで増えるなら助し、たさないほうが高い時はたさない
    dp[i+1] = dp[i] + a[i] | dp[i]
    '''
    for i in range(n):
        line = []
        print("  w[i],v[i] : (" + str(a[i][0]) +", " + str(a[i][1]) + ")")
        for j in range(w+1):
            #print_line = 'w : ' + str(j) + '　までで,  w[i],v[i] : (' + str(a[i][0])+ ", " + str(a[i][1]) +') は積める？'

            if(j >= a[i][0]):
                print("nap : " + str(dp[i][j-a[i][0]]))
                print("weg : " + str(a[i][1]))
                print("add : " + str(dp[i][j-a[i][0]] + a[i][1]))

                line.append(choice_max(dp[i][j-a[i][0]] + a[i][1], dp[i][j]))
                #print_line += '  -> 詰める'
            else:
                #print_line += '  -> 詰めない'
                line.append(dp[i][j])

            #print(print_line)
            print('- - - - - - - - - ')

        dp.append(line)
        print('-**----***-----***--**----')

    print(*a, sep='\n')
    #DP table
    print(*dp, sep='\n')
    #answer
    print(dp[n][w])

if __name__ == '__main__':
    n = 6
    w = 9
    a = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]

    solve(n, w, a)
