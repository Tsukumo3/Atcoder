n = int(input())
a = list(map(int, input().split()))

m = [0 for i in range(n)]

for i in a:
    m[i-1] += 1

print(*m, sep='\n')
