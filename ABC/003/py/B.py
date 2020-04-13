s = input()
t = input()

a_dict = ["a", "t", "c", "o", "d", "e", "r"]

flag = True

for i in range(len(s)):
    if s[i] == "@" and t[i] in a_dict:
        continue
    elif t[i] == "@" and s[i] in a_dict:
        continue
    elif s[i] == t[i]:
        continue

    elif t[i] == "@" and not s[i] in a_dict:
        flag = False
        break
    elif s[i] == "@" and not t[i] in a_dict:
        flag = False
        break
    elif t[i] == "@" and not s[i] in a_dict:
        flag = False
        break
    elif s[i] != t[i]:
        flag = False
        break

if flag:
    print("You can win")
else:
    print("You will lose")
