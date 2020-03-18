class UnionFindTree():
    '''ランク付きUnionFind木'''
    def __init__(self, n):
        #親の番号
        self.par = list(range(n))
        self.rank = [0] * n

    def root(self, x):
        #木の根を求める
        if self.par[x] == x:#自分が根ノードなら
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        #木の高さ-ランクが低い方に繋げる
        if self.rank[x] < self.rank[y]:
            self.par[x] = y # 低いxにyを繋げる
        else:
            self.par[y] = x # 逆
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        #xとyが同じ集合に属するか
        #print(x,self.root(x), " : ", y,self.root(y))
        print(1) if self.root(x) == self.root(y) else print(0)

def querying(queries, uft):
    for query in queries:
        if query[0] == 0:#unite
            uft.unite(query[1], query[2])
            print(uft.par, " : ", query[1]," : ", query[2])
        else:
            uft.same(query[1], query[2])

if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]
    #instant UnionFindTree
    uft = UnionFindTree(n)
    #Querying
    querying(queries, uft)
