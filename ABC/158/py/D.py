from collections import deque
s = deque()
s.append(input())
q = int(input())
lines = [list(input().split()) for i in range(q)]
def q1(s):
    for i in range(len(s) // 2):
        s[i],s[-1-i] = s[-1-i],s[i]
    return s

def q2(s, l, flag):
    if int(l[1]) == 1:
        if flag:
            s.append(l[2])
        else:
            s.appendleft(l[2])
    else:
        if flag:
            s.appendleft(l[2])
        else:
            s.append(l[2])
    return s
flag = False
count = 1
for l in lines:
    if int(len(l)) == 1:
        flag = True
        count += 1
    else:
        q2(s, l, flag)
        flag = False


print(*s, sep='')
