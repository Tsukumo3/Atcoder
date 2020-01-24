predict = list(input())
result = list(input())

count = 0

for i in range(len(predict)):
    if predict[i] == result[i]:
        count += 1

print(count)
