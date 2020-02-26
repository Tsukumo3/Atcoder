import queue

class Solution():
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
        #フィールド
        self.field = []
        #キュー
        self.q = queue.Queue()
        #start
        self.start = []

        self.vectors = [[1,0],[-1,0],[0,1],[0,-1]]

    class Bit():
        def __init__(self, tag, x, y):
            self.tag = tag
            self.point = [x, y]
            self.cost = -1#未踏
            self.isVisited = False

        def __str__(self):
            #return self.tag +" : "+ str(self.point[0])+", " + str(self.point[1])
            return self.tag

    def make_field(self):
        for i in range(m):
            line = []
            for j in range(n):
                line.append(self.Bit(a[i][j],i,j))
                #start地点は全ての"."
                if a[i][j] == ".":
                    self.start.append((i, j))

            self.field.append(line)

    def push_next_points(self, now):

        for i in self.vectors:
            # tryでindexがなしを解消
            if now.point[0] + i[0] >= 0 and now.point[0] + i[0] < m:
                if now.point[1] + i[1] >= 0 and now.point[1] + i[1] < n:
                    if self.field[now.point[0] + i[0]][now.point[1] + i[1]].tag == "#":
                        continue
                    else:
                        if self.field[now.point[0] + i[0]][now.point[1] + i[1]].isVisited == False:
                            self.field[now.point[0] + i[0]][now.point[1] + i[1]].isVisited = True
                            self.field[now.point[0] + i[0]][now.point[1] + i[1]].cost = now.cost + 1
                            self.q.put(self.field[now.point[0] + i[0]][now.point[1] + i[1]])

    def loop(self):
        # 3 キューからデータがなくなるまで取り出しを行う
        max = 0
        while not self.q.empty():
            now = self.q.get()
            #print(now)
            # 3.1 取り出しますが亡くなった時の最大値を考える
            #if now.tag == "g":
                #return now.cost
                #break
            if max < now.cost:
                max = now.cost

            # 3.2 取り出したマスから上下左右にcostを代入し、queueに入れる
            self.push_next_points(now)

        return max


    def solve(self):

        # field作成 &
        self.make_field()
        # 初期設定   ::  startをqueueに入れる
        max = 0
        for point in self.start:
            self.field[point[0]][point[1]].cost = 0
            self.field[point[0]][point[1]].isVisited = True
            self.q.put(self.field[point[0]][point[1]])
            # queが空になるまで繰り返す
            ans = self.loop()
            if max < ans:
                max = ans


            print("- - start(0)からのgまでの最短距離 - -")
            for i in self.field:
                for j in i:
                    print(j.cost , end = " ")
                print("")
            

        print(max)


if __name__ == '__main__':

    #n横 m縦
    m, n = map(int, input().split())
    # 1 迷路の作成と探索履歴の作成
    a = [list(input()) for i in range(m)]

    Solution = Solution(n, m, a)
    Solution.solve()
