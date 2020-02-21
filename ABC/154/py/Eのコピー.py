n = input()
k = int(input())
'''
dp0[i][j] =上からi桁目まで決めて、0でない桁がj個あり、
            Nより小さいことが確定している

dp1[i][j] =上からi桁目まで決めて、0でない桁がj個あり、
            Nより小さいことが確定していない
'''
k_list = [ 0 for i in range(k+1) ]

dp0 = [ [ 0 for i in range(k+1) ] for i in range(len(n)+1) ]
dp1 = [ [ 0 for i in range(k+1) ] for i in range(len(n)+1) ]

#[print(dp) for dp in dp0]

num = list(range(0,10))

#初期条件
dp0[0][0] = 1
dp1[0][1] = 1

for i, c in enumerate(n):
    '''
    print("- - - - - - -")
    [print(item) for item in dp0]
    print("- - - - - - -")
    [print(item) for item in dp1]
    print("- - - こうしん - - -")
    '''

    #print(i, c)
    #less = num[:int(c)]
    #equal = int(c)

    for j in range(k+1):

        #0を系列に追加
        if j == 0:
            dp0[i+1][j] = 1
        #1~9までの系列に0を追加したものと、0系列に1~9を追加数r
        else:
            if i == 0 and j == 1:
                dp0[i+1][j] = int(c) - 1
                #print(j, dp0[i+1][j], int(c) - 1)
            else:
                dp0[i+1][j] = dp0[i][j] + dp0[i][j-1]*9

        #0を系列に追加
        if j == 1:
            dp1[i+1][1] = 1
        #1~9までの系列に0を追加したものと、0系列に1~9を追加数r
        elif j != 0:
            if i == 0 and j == 2:
                print("int(c) - 1 :" + str(int(c) - 1))
                dp1[i+1][j] = int(c)
            else:
                dp1[i+1][j] = dp1[i][j] + dp1[i][j-1]*int(c)

print(" - - - 結果 - - -")
[print(item) for item in dp0]
print("- - - - - - -")
[print(item) for item in dp1]
print("anser k = " + str(k))

print(dp0[len(n)][k] + dp1[len(n)][k])
