n = input()
k = int(input())
'''
dp0[i][j] =上からi桁目まで決めて、0でない桁がj個あり、
            Nより小さいことが確定している

dp1[i][j] =上からi桁目まで決めて、0でない桁がj個あり、
            Nより小さいことが確定していない
'''
k_list = [ 0 for i in range(k+1) ]

dp0 = [ k_list for i in range(len(n)+1) ]
dp1 = [ k_list for i in range(len(n)+1) ]

#[print(dp) for dp in dp0]

number = list(range(0,10))

for i in range(int(n)):
    for j in range(k+1):

        num = number[0,n[i]]

        #0でない個数が0 -> 次の値も0
        if j == 0:
            dp0[i+1][0] = dp[i][0]

            dp0[i+1][j] = dp[i][j]
