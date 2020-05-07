n, a, b, c = map(int, input().split())
s = [input() for i in range(n)]
log = []

def end():
    print("No")
    exit()

def under_zero(x):
    if x < 0:
        return True
    else:
        return False

def solve(string,a,b,c):

    if string == "AB":
        if a>=b:
            a -= 1
            b += 1
            log.append("B")
            if under_zero(a):
                return end()
        else:
            a += 1
            b -= 1
            log.append("A")
            if under_zero(b):
                return end()
    elif string == "AC":
        if a>=c:
            a -= 1
            c += 1
            log.append("C")
            if under_zero(a):
                return end()
        else:
            a += 1
            c -= 1
            log.append("A")
            if under_zero(c):
                return end()
    else:
        if b>=c:
            b -= 1
            c += 1
            log.append("C")
            if under_zero(b):
                return end()
        else:
            b += 1
            c -= 1
            log.append("B")
            if under_zero(c):
                return end()

def check(i,a,b,c):
    now = list(s[i])
    next = list(s[i+1])

    for i in now:
        if i in next:
            d = i

    #print(d)

    # 連続でAが来る
    if 'A' == d and now[1] == 'B':
        a += 1
        b -= 1
        log.append("A")

    elif 'A' == d and now[1] == 'C':
        a += 1
        c -= 1
        log.append("A")

    # bが重複
    if 'B' == d and now[0] == 'A':
        a -= 1
        b += 1
        log.append("B")

    elif 'B' == d and now[1] == 'C':
        b += 1
        c -= 1
        log.append("B")

    # cが重複
    if 'C' == d and now[0] == 'A':
        c += 1
        a -= 1
        log.append("C")

    elif 'C' == d and now[0] == 'B':
        c += 1
        b -= 1
        log.append("C")

    return

for i in range(n):
    if i != n-1:
        if (a + b + c) == 2 and (a == 1 and b == 1) or (a == 1 and c == 1) or (c == 1 and b == 1):
            check(i,a,b,c)
    else:
        solve(s[i],a,b,c)
else:
    print("Yes")
    print(*log, sep='\n')
