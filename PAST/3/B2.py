n ,m ,q = map(int, input().split())
s = [list(map(int, input().split())) for i in range(q)]

for i in range(q):
    s[i][1] -= 1

    if len(s[i]) == 3:
        s[i][2] -= 1

score = [0 for i in range(n)]
num = [[] for i in range(m)]

for i in s:
    if i[0] == 1:
        print(score[i[1]])

    elif i[0] == 2:
        #すでに解いてるやつ減算
        length = len(num[i[2]])
        for j in range(length):
            score[ num[i[2]][j] ] -= 1

        #追加
        num[i[2]].append(i[1])
        score[i[1]] += n - length - 1
