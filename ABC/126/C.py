A, B, X = map(int, input().split())

#N円買うには A*N + B * (Nの桁数)円
#N = 10 A* 10 + 7 * 2

#上限
if(X = 1000000000):
    print(1000000000)

#A*N + B*len(N)
