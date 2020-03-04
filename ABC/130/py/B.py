n, x = map(int, input().split())
l = list(map(int, input().split()))
cumlate = [0]*(n+1)
for i in range(n):
    cumlate[i+1] = cumlate[i] + l[i]
    if x < cumlate[i+1]:
        print(i+1)
        exit()
else:
    print(n+1)
