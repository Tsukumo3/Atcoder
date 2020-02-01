H ,N = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]

time = 0


#print(AB)


for i in range(N):
    AB[i].append(AB[i][0]/AB[i][1])

#[print(i) for i in AB]

costAB = sorted(AB,key=lambda x:(-x[2],x[0]))

#[print(i) for i in costAB]

MP=0

for i in range(N):
    if not i == 0:
        cost1 = costAB[i-1][0]

        time2 = H//costAB[i][0]
        cost2 = time*costAB[i][1]

        if cost1 <= cost2:
            MP += cost1
            break
        else:
            MP += cost2
            H = H%costAB[i][1]

    else:
        time = H//costAB[i][0]
        MP += time*costAB[i][1]
        H = H%costAB[i][1]

print(MP)
