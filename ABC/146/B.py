N = int(input())
S = list(input())

alf = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

slide = alf[N:] + alf[:N]

ans = []

for i in S:
    l = alf.index(i)
    t = slide[l]
    ans.append(t)

print("".join(ans))
