number = int(input())
lower = list(map(int, input().split()))

time = 0
max = 0

def down(i):
    global time
    for j in range(i, number-1):
        if lower[j] >= lower[j+1]:
            time += 1
        else:
            return j+1

    return 0

now = 0
for i in range(len(lower)):

    if now > i:
        continue

    if max > (number-i+1):
        break

    now = down(i)

    if max < time:
        max = time
    time = 0



print(max)
