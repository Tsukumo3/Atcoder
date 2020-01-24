N = int(input())
S = input()

import re

pattern = "ABC"

item = re.findall(pattern, S)

print(len(item))
