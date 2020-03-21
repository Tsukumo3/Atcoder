n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
ans = True
for i in l:
    t, x, y = i[0], i[1], i[2]
    if x+y > t or (x+y)%2 != t%2:
        ans = False

print("Yes") if ans else print("No")
