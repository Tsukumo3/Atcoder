def dijkstra(s,n,w,cost,mochi, time):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    have = mochi

    while True:
        print(used)
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True

        for j in range(n):
                #d[j] = min(d[j],d[v]+cost[v][j][1])
                print("have: ", have, ", ",v," to ",j, "cost: ", cost[v][j][1])
                if have >= cost[v][j][0]:
                    d[j] = min(d[j],d[v]+cost[v][j][1])
                    print("go", d[j])
                elif v != j:
                    d[j] = min(d[j],d[v]+cost[v][j][1] + time[v][1])
                    have += time[v][0]
                    print("exchange", d[j])
        print("one-- - ")
        have = mochi
    return d

################################
n,m,s = map(int,input().split()) #n:頂点数　m:辺の数 s:銀貨の枚数

cost = [[(10**5,10**5) for i in range(n)] for i in range(n)]
#cost[u][v] : 辺uvのコスト(存在しないときはinf この場合は10**10)
time = [[0,0] for i in range(n)]

for i in range(m):
    x,y,a,b = map(int,input().split())
    cost[x-1][y-1] = (a,b)
    cost[y-1][x-1] = (a,b)

for i in range(n):
    c,d = map(int, input().split())
    time[i] = [c,d]

print(dijkstra(0,n,m,cost,s,time))
