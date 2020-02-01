H = int(input())

time = 0
now = H
pow2list = [2**i for i in range(50)]

import math
a = math.log(now, 2)
print(sum(pow2list[0:math.floor(a+1)]))
