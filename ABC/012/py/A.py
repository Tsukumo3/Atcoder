kk = 0
for i in range(1, 10):
    for j in range(1, 10):
        kk += i*j

N = int(input())

m = kk - N

ans = []
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == m:
            ans.append([i,j])
ans.sort()
for i in ans:
    s = str(i[0]) + " x " + str(i[1])
    print(s)
