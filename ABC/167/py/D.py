"""
最初からループ
4 5
3 2 4 1
out 4: ok

途中からループ

ループまで行かず
6 1
6 5 2 5 3 2

out 6: ok

ループまで行く
6 727202214173249351
6 5 2 5 3 2

out: 2 : ok

"""

def looptime(n, a):
    for i in range(n):
        loop = 0
        start = i
        now = i

        time = 0

        while(loop < n):
            now = a[now]
            loop += 1
            now -= 1

            if now == start:
                return i+1, loop

def start_loop(goal, a):
    loop = 0
    now = 0

    time = 0

    while(loop < n):
        now = a[now]
        loop += 1
        now -= 1

        if now == goal-1:
            return loop

if __name__ == '__main__':

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    start, loop = looptime(n, a)
    how = start_loop(start, a)
    point = k%loop
    #print(start, loop, point, how)

    if how == loop:
        # startからループ開始
        time = 0
        now = 0
        while(time < point):
            now = a[now]
            now -= 1
            time += 1
        print(now+1)

    else:
        # 途中からループ開始
        if how > k:
            time = 0
            now = 0
            while(time < k):
                now = a[now]
                now -= 1
                time += 1
            print(now+1)

        else:
            time = 0
            now = start-1
            point = (point+how)%loop
            while(time < point-1):
                now = a[now]
                now -= 1
                time += 1
            print(now+1)
