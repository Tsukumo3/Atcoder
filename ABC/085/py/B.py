import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for i in range(n)]
d.sort()

#初期値
now = d.pop() #一番大きい値
ans = 1 # １段目
#print(" ")
while len(d) != 0:
    next = d.pop()
    #print(next)
    if now > next:
        ans += 1
        now = next

print(ans)
