S = list(input())
T = list(input())

S.sort(reverse=False)
T.sort(reverse=True)

S_str = "".join(S)
T_str = "".join(T)

if S_str < T_str:
    print("Yes")
else:
    print("No")
