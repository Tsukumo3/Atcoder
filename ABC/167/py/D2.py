def loops(n,a):

    loop = 0
    now = 0
    time = 0

    g = [False]*n
    g[0] = True

    while(True):
        now = a[now]
        loop += 1
        now -= 1

        if not g[now]:
            g[now] = True
        else:
            return now+1 ,loop

def start_loop(goal, a):
    loop = 0
    now = 0

    time = 0

    while(loop <= n):
        now = a[now]
        loop += 1
        now -= 1

        if now == goal-1:
            return loop+1

if __name__ == '__main__':

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    start, loop = loops(n, a)

    how = start_loop(start, a)

    loop = how

    ans = (k-how)%loop

    if k < how:
        

    print(ans)
