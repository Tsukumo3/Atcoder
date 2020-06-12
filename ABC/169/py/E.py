n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

front = sorted(l, key=lambda x:x[0])
back = sorted(l, key=lambda x:-x[1])

print(front)
print(back)

center = n//2+n%2-1
print(center,front[center][0], back[center][1])
ans = abs(front[center][0]- back[center][1])*2+1
print(ans)
