N ,M = map(int, input().split())
ps = [list(input().split()) for i in range(M)]

ac = [0 for i in range(N)]
wa = [0 for i in range(N)]

for i in range(M):
    s = int(ps[i][0])-1
    if ps[i][1] == "WA" and ac[s] == 0:
        wa[s] += 1

    if ps[i][1] == "AC" and ac[s] == 0:
        ac[s] = 1

for i in range(N):
    if ac[i] == 0:
        wa[i] = 0

print(str(sum(ac)) + " " + str(sum(wa)))
