l = map(int, input().split())

from collections import Counter

c = Counter(l)

for i in c.items():
    if i[1] == 1 or i[1] == 3:
        print(i[0])
        exit()
