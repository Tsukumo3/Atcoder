n, x, y = map(int, input().split())

#1
line = [0 for i in range(n)]
#line[0] = n
tree = [[] for i in range(n)]
for i in range(n-1):
    tree[i].append(i+1)
tree[x-1].append(y-1)
print(tree)

def bfs(s, t):

    g = [None for i in range(n)]
    g[s] = 0

    for i in tree[s]:
        if g[i] == None:
            g[i] = +1



for i in range(n-1):
    bfs(i, 0)

print(*line, sep='\n')
