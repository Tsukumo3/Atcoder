n = int(input())

ans_mod26 = []

while(n > 26):
    ans_mod26.append(n//26)
    n -= n//26

print(ans_mod26)
