N = int(input())
#i番目の人の証言
tests = []
#i番目の人はTrue
TorF = [1 for i in range(N)]

for i in range(N):
    A = int(input())
    xy_list = [list(map(int, input().split())) for i in range(A)]
    tests.append(xy_list)


#全ての証言が正しかったと仮定した場合から順々に減らしていく？
#N n-1 n-2 /// 1 
for i in range(N):
    for j in range(len(tests[i])):
        #print(tests[i][j])
        x, y = tests[i][j][0], tests[i][j][1]

        if y == 0:
            TorF[x-1] = 0

print(sum(TorF))
