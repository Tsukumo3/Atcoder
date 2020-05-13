s = input()
t = input()

if s == t[:-1] and len(s) == len(t)-1:
    print("Yes")
else:
    print("No")
