n = int(input())
games = [list(map(int, input().split())) for i in range(n)]

action = []

days = 0

battleLog = [0 for i in range(n)]

flag = False

while(True):

    flag = False

    days += 1

    for i in range(n):
        
        for j in range(i+1,n):

            if(i in action or j in action):
                continue

            if(battleLog[i] == n-1 or battleLog[j] == n-1):
                continue

            #試合相手とプレイヤー名が互いに一致している場合において決闘開始
            if(games[i][battleLog[i]] == j+1 and games[j][battleLog[j]] == i+1):

                #print("試合 : " +str(i+1) + " : " + str(j+1))

                battleLog[i] += 1
                battleLog[j] += 1

                action.append(i)
                action.append(j)

                flag = True

                break


    action.clear()

    if battleLog.count(n-1) == n:
        break

    if not flag:
        days = -1
        break

print(days)
