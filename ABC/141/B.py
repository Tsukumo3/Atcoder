#https://atcoder.jp/contests/abc141/tasks/abc141_b

c = input()

ans = "Yes"
odd = ['R','U','D']
eval = ['L','U','D']
for i in range(len(c)):
    if i % 2 == 0 and not c[i] in odd:
        ans = "No"
    elif i % 2 == 1 and not c[i] in eval:
        ans = "No"
print(ans)
