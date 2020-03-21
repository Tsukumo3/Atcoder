import re# regular expression
s = input()
m = re.fullmatch(r'(dream(er)?|erase(r)?)+', s)
#print(m)
#print(type(m))
if m == None:#マッチ無し
    print("NO")
else:#フルマッチあり
    print("YES")
