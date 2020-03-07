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

print("- - - - - - -")
print(*tb, sep="\n")

q = deque()

for i in range(n):
    for j in range(i+1, n):
        if tb[i][j] == None:
            q.append((i, j))

ans = [0 for i in range(n)]

while q:
    now = q.popleft()

    for i in range(n):
        #人iがnow[0]とnow[1]と友達だったら推薦
        if tb[i][now[0]] == 1 and tb[i][now[1]] == 1 :
            ans[now[0]] += 1
            ans[now[1]] += 1
    
print(*ans, sep=" ")
