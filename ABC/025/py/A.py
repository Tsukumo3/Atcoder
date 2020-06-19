import itertools

x = input()
n = int(input())

p = list(itertools.product(x, repeat = 2))

print("".join(p[n-1]))
