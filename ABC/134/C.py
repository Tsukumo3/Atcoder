n = int(input())
a = [int(input()) for i in range(n)]

max_value = max(a)
max_index = a.index(max_value)

for i in range(n):
    if not i == max_index:
        print(max_value)
    else:
        newlist = a[:i] + a[i+1:]
        print(max(newlist))
