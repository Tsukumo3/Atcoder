from collections import deque

n, m, k = map(int, input().split())
fr = [list(map(int, input().split())) for i in range(m)]
br = [list(map(int, input().split())) for i in range(k)]

tb = [[None]*n for i in range(n)]
# 友達登録
for i in range(m):
    tb[fr[i][0]-1][fr[i][1]-1] = 1
    tb[fr[i][1]-1][fr[i][0]-1] = 1
# ブロック登録
for i in range(k):
    tb[br[i][0]-1][br[i][1]-1] = -1
    tb[br[i][1]-1][br[i][0]-1] = -1
# 自分は無視
for i in range(n):
    tb[i][i] = 0

#print("- - - - - - -")
#print(*tb, sep="\n")

def dfs_check():
    ans = [0 for i in range(n)]

    for i in range(n):
        #print("-- ",i+1,"の友達候補探し")
        #表の初期化
        g = [None for i in range(n)]

        stack = deque()
        stack.append(i)
        #最初の地点のコストは0
        g[i] = 0

        while stack:
            k = stack.pop() #stackから取り出す
            move = [d for d in range(n) if tb[k][d] == 1]#友達なら移動
            #moveprint = [d+1 for d in range(n) if tb[k][d] == 1]
            #print(k+1, "の友達", moveprint)
            for dk in move:
                if g[dk] == None:
                    g[dk] = 1
                    stack.append(dk)
                    if tb[i][dk] == None:
                        #print(i+1,dk+1,"は友達！")
                        ans[i] += 1
    return ans

#友達を辿ってたどり着けるところまで考える
print(*dfs_check(), sep=" ")
