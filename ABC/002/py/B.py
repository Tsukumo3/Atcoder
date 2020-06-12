w = input()
ans = []
subset = ["a", "i", "u", "e", "o"]
for c in w:
    if not c in subset:
        ans.append(c)

print(*ans, sep = "")
