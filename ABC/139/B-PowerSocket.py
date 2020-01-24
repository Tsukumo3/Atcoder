list = list(map(int, input().split()))

amount = 1
count = 0

while list[1] > amount:
    count += 1
    amount += list[0] - 1

print(count)

#　加算していくとACする…どういうこと…
