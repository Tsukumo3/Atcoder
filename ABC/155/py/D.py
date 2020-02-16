'''
n = int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [int(input()) for i in range n]
p = [list(map(int, input().split()))]

a = input()
a, b = input().split()
a = [input() for i in range n]
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))

mins = []
plus = []
zero = []

for i in a:
    if i > 0:
        plus.append(i)
    elif i < 0:
        mins.append(i)
    else:
        zero.append((i))

ans = 0

def degree(a):
    return a*(a+1)//2

def divlist1(a,b):
    _len = len(a)
    return [i*j for i in a for j in b]

def divlist2(a):
    _len = len(a)
    return [a[i]*a[j] for i in range(_len-1) for j in range(i+1, _len)]

pattarn = degree(n)
plus_p = degree(len(plus)) + degree(len(mins))
mins_p = len(mins)+len(plus)
zero_p = pattarn-(plus_p+mins_p)

print(pattarn,plus_p,zero_p,mins_p)

if k <= pattarn//2:
    #下から
    if mins_p >= k:
        _list = divlist1(mins,plus)
        _list.sort()
        print(_list)
        ans = _list[k-1]

    elif mins_p+zero_p >= k:
        ans = 0

    else:
        _list = divlist2(plus)
        _list.extend(divlist2(mins))
        ans = _list[k-1-mins_p-zero_p]

print(ans)
