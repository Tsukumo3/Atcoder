n ,m ,q = map(int, input().split())
s = [input().split() for i in range(q)]

score = [[0 for i in range(m)] for i in range(n)]

num = [[] for i in range(n)]

for i in s:
    if i[0] == "1":
        print(sum(score[int(i[1])-1]))

    elif i[0] == "2":
        num[int(i[2])-1].append(int(i[1])-1)


        for j in range(len(num[int(i[2])-1])):
            score[ num[ int(i[2])-1 ][j]][int(i[2])-1] = n - len(num[int(i[2])-1])

        #print(num)
        #print(score)
