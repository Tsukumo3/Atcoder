'''
n = int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [int(input()) for i in range n]
p = [list(map(int, input().split()))]

a = input()
a, b = input().split()
a = [input() for i in range n]

全探索！！


'''
n = int(input())
x = list(map(int, input().split()))
cost = 10**9
for i in range(1,100):
    now = 0
    for j in x:
        now += (i-j)**2
    if cost > now:
        cost = now
print(cost)
