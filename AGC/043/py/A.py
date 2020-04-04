from collections import deque

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

def route():
    i, j = (0, 0)
    q = deque()
    q.append(start)

    move = ((0, -1), (1, 0))#右と下
    while q:
        i, j = q.pop()#que左端から取り出す
        for di, dj in move:
            #ni, nj 遷移先の座標
            ni , nj = i + di, j + dj
            #遷移先がフィールド内であるか、Noneかどうかをチェックする
            if ni < h and  nj < w:
                if s[ni][nj] == ".":
                    q.append((ni, nj))
    #止まり次第






ans = route()
print(ans)
