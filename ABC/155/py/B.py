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

n = int(input())
a = list(map(int, input().split()))

ans = "APPROVED"
#DENIED
for i in a:
    if i%2 == 1:
        continue
    elif i%3 == 0:
        continue
    elif i%5 == 0:
        continue
    else:
        ans = "DENIED"

print(ans)
