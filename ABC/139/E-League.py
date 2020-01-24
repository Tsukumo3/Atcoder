n = int(input())
games = [list(map(int, input().split())) for i in range(n)]

action = []

days = 0


while(True):

    for i in range(n):

        for j in range(i+1,n):

            if i in action:
                continue

            if j in action:
                continue

            print("games[" + str(i) +"][0] = " + str(games[i][0]))
            print("j+1 = " + str(j+1))

            if games[i][0] == j+1:

                print("試合 : " +str(i+1) + " : " + str(j+1))

                games[i].pop(0)
                games[j].pop(0)

                action.append(i)
                action.append(j)
                print(" ")

    days += 1
    action.clear()

    if len(games) == 0:
        break

print(days)
