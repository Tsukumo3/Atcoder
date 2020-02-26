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
n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    print(100*(10-n) + r)
