n = int(input())
arrayB = list(map(int, input().split()))

arrayA = [arrayB[0]]

for k in range(1,n-1):

    if arrayB[k] < arrayB[k-1]:
        arrayA.append(arrayB[k])

    else:
        arrayA.append(arrayB[k-1])

arrayA.append(arrayB[n-2])

print(sum(arrayA))
