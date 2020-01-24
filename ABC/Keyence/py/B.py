N = int(input())
robots = [list(map(int,input().split())) for i in range(N)]
table = []
coli = [0 for i in range(N)]

robots.sort(key=lambda x:x[0])

for i in range(N):
    right_arm = robots[i][0] + robots[i][1]
    left_arm = robots[i][0] - robots[i][1]
    table.append([left_arm,right_arm])

for i in range(N-1):
    #あたってるか判定
    #あたってたら右隣を1
    if coli[i] == 1:
        continue

    right_arm = robots[i][0] + robots[i][1]
    left_arm = robots[i+1][0] - robots[i+1][1]

    if right_arm > left_arm:
        coli[i+1] = 1

print(N-sum(coli))
