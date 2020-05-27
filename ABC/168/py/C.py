a,b,h,m = map(int, input().split())


phi = m * 6

theta = h * 30 + 0.5 * m

import math

apoint = (a*math.cos(math.radians(theta)), a*math.sin(math.radians(theta)))
bpoint = (b*math.cos(math.radians(phi)),   b*math.sin(math.radians(phi)))

#print(theta,phi, apoint, bpoint)

xd = abs(apoint[0] - bpoint[0])
yd = abs(apoint[1] - bpoint[1])

#print(xd, yd)

ans = math.sqrt(math.pow(xd,2) + math.pow(yd,2))

print(ans)
