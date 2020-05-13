
inf = pow(10, 9) + 7

def solve(m, x, bag):

    p = [0]*(m+1)

    for i in range(len(bag)):
        for j in range(m+1):
            p[j] += bag[i][j]

    for i in range(1,m+1):
        if p[i] < x:
            return inf
    else:
        return p[0]

if __name__ == '__main__':

    n, m, x = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]

    mini = inf

    for i in range(2**n):
        bag = []
        #print("p{} : ".format(i), end="")

        for j in range(n):
            if((i >> j) & 1):
                bag.append(l[j])
        #print(bag)
        r = solve(m, x, bag)
        if mini > r:
            mini = r

    if mini == inf:
        print(-1)
    else:
        print(mini)
