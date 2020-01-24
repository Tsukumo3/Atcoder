colors = list(map(int, input().split()))

ans = []

for i in colors:
    if not i in ans:
        ans.append(i)

print(len(ans))
