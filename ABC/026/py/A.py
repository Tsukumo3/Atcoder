n = int(input())
max = 0
for i in range(1,n+1):
    j = n-i
    if max < i*j:
        max = i*j
print(max)
