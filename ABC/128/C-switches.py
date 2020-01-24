class switch:
    def __init__(self,name):
        self.name = name
        self.flag = False

class right:
    def __init__(self,name):
        self.name = name
        self.component = []
        self.condition = 0
        self.isBright = False

    def setConponent(self,component):
        self.component = component

    def setCondition(self,condition):
        self.condition = condition

    def setIsBright(self,isBright):
        self.isBright = isBright




def main():
    n,m =map(int,input().split())
    dataS = [list(map(int , input().split())) for i in range(m)]
    dataR = list(map(int , input().split()))

    switch_list = [switch(i+1) for i in range(n)]
    right_list = [right(i+1) for i in range(m)]

    for i in range(m):
        #switch[i]番目の操作
        swNum = dataS[i][0]

        swl = []
        for j in range(swNum):
            swName = dataS[i][j+1]
            sw = switch_list[swName-1]
            swl.append(sw)
        right_list[i].setConponent(swl)

    for i in range(m):
        right_list[i].setCondition(dataR[i])

    #操作
    #全てが点灯する条件
    #->前から点灯させていく->条件が増えていく動的計画?

    for r_i in right_list:
        for s_i in r_i.component:







if __name__ == "__main__":
    main()
