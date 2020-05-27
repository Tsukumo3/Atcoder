n = int(input())
s = [set(list(input())) for i in range(n)]
ans = [""]*n

if n%2 == 1:
    length = n//2+1
else:
    length = n//2

for i in range(1, 1+length):

    intersection = s[i-1] & s[-i]

    if len(intersection) == 0:
        print(-1)
        exit()

    item = intersection.pop()

    ans[i-1], ans[-i] = item, item

print(*ans, sep='')
