import math
a,b = map(int, input().split())

max = math.floor(100*1.08)

for i in range(1,max+1):

    if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
        print(i)
        exit()
print(-1)
