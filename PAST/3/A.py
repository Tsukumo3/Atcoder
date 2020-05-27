s = input()
t = input()

if s == t:
    print("same")
elif str.lower(s) == str.lower(t):
    print("case-insensitive")
else:
    print("different")
