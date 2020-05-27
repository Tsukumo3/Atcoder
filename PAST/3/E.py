n, m ,q = map(int, input().split())
vm = [list(map(int, input().split())) for i in range(m)]
c = [0] + list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(q)]

g = [[] for i in range(n+1)]
for i in range(m):
    g[vm[i][0]].append(vm[i][1])
    g[vm[i][1]].append(vm[i][0])

for i in range(q):
    if s[i][0] == 1:
        print(c[s[i][1]])
        for j in g[s[i][1]]:
            c[j] = c[s[i][1]]

    else:
        print(c[s[i][1]])
        c[s[i][1]] = s[i][2]
