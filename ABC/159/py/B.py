s = input()
s1 = s[:(len(s)-1)//2]
s2 = s[(len(s)+3)//2-1:]

flag = True
# [:] の指定は　左が閉区間、右が開区間 [ )こんな感じ
if s != s[::-1]:
    flag = False
if s1 != s1[::-1]:
    flag = False
if s2 != s2[::-1]:
    flag = False
print("Yes") if flag else print("No")
