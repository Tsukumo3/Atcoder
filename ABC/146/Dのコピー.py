def main():
    N = int(input())
    lines = [list(map(int, input().split())) for i in range(N-1)]

    nodes = [[] for i in range(N)]

    for l in lines:

        nodes[l[0]-1].append(l[1])
        nodes[l[1]-1].append(l[0])

    max = 0
    for n in nodes:
        if max < len(n):
            max = len(n)

    #色の数
    print(max)

    #関係の数字
    count = [0 for i in range(N)]

    for l in lines:

        count[l[0]-1]+=1
        count[l[1]-1]+=1

        print(count[l[0]-1])

    print(count)





if __name__ == '__main__':
    main()
