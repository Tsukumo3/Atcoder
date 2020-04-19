import re# regular expression
s = "3:fizz 5:buzz 1"
m = re.fullmatch(r'[1-9]([0-9])*:[a-zA-Z]+', s)
#print(m)
#print(type(m))
if m == None:#マッチ無し
    print("NO")
else:#フルマッチあり
    print("YES")
