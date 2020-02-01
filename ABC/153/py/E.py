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

for i in costAB:
    if H <= 0:
        break
    while True:
        if H <= i[0]:
            break
        else:
            H -= i[0]
            MP += i[1]
print(H)
print(MP)
minAB = [i[1] for i in AB]
min_magic = min(minAB)
print(MP+min_magic)
