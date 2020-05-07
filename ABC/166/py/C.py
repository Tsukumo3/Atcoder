n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]

f = [[] for i in range(n)]

for i in ab:
    f[i[0]-1].append(i[1]-1)
    f[i[1]-1].append(i[0]-1)
ans = 0
#print(f)
for i in range(n):
    flag = True
    for j in range(len(f[i])):
        #print("比べ,",i,f[i][j], h[i], h[f[i][j]])
        if h[i] <= h[f[i][j]]:
            #print("低い")
            flag = False
            break
    if flag:
        #print("good",i)
        ans += 1

print(ans)
