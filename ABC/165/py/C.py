n, m, q = map(int, input().split())
x = [list(map(int, input().split())) for i in range(q)]

def solve(pas, max):
    a = [None]*n
    a[0] = 1

    cnt = 0

    if a[x[pas][0]-1] == None:
        a[x[pas][0]-1] = x[pas][0]-1

    if a[x[pas][1]-1] == None:
        a[x[pas][1]-1] = a[x[pas][0]-1] + x[pas][2]

    for i in range(q):
        if a[x[i][0]-1] == None:
            a[x[i][0]-1] = x[i][0]-1

        if a[x[i][1]-1] == None:
            a[x[i][1]-1] = a[x[i][0]-1] + x[i][2]

        #print(a[x[i][1]-1], a[x[i][0]-1] ,"== ",x[i][2], " :" , x[i][3])
        #print(a[x[i][1]-1] - a[x[i][0]-1] == x[i][2])
        if a[x[i][1]-1] - a[x[i][0]-1] == x[i][2]:
            cnt += x[i][3]

    #print(cnt)

    if max < cnt:
        max = cnt
    return max

max = 0
for i in range(q):
    max = solve(i, max)
print(max)
