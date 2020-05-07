x = int(input())
# 1 <= x <= 10^9
for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        if pow(i,5) - pow(j,5) == x:
            print(i, j)
            exit()
