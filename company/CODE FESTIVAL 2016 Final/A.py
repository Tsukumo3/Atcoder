alf = list("abcdefghijklmnopqrstuvwxyz")

h, w = map(int, input().split())

for i in range(h):
    line = list(input().split())
    if "snuke" in line:
        x = line.index("snuke")
        y = i

print(alf[x].upper(),y+1, sep='')
