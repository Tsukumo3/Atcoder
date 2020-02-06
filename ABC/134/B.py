N, D = map(int,input().split())

reach = D*2+1
import math
minimum = math.ceil(N/reach)
print(minimum)
