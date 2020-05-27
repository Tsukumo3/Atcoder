import collections

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(m)]

    ways = [[] for i in range(n+1)]

    for i in l:
        ways[i[0]].append(i[1])
        ways[i[1]].append(i[0])

    #print(ways)

    q = collections.deque()

    ans = [-1] * n # 道案内
    ans[0] = 0

    q.append(1)

    while(len(q) != 0):
        item = q.popleft()
        for i in ways[item]:
            if ans[i-1] == -1:
                ans[i-1] = item
                q.append(i)
                #print(ans , i , item)

    if -1 in ans:
        print("No")
    else:
        print("Yes")
        for i in range(1,n):
            print(ans[i])
