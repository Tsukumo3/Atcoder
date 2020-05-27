import collections

n = int(input())
a = [int(input()) for i in range(n)]

cnt = [0]*n

dup = None
no = None

for i in range(n):
    cnt[a[i]-1] += 1

try:
    no = cnt.index(0)
    dup= cnt.index(2)
except ValueError:
    pass

if dup != None:
    print(dup+1, no+1)
else:
    print("Correct")
