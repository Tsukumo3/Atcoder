import math
a, b , n = map(int, input().split())

#初期値
left = 0
right = pow(10,12)

while(left < right):

    mid = left + (right - left)//2
    print(mid)
    max = math.floor(a*mid/b) - a * math.floor(mid/b)

    #right
    r = right + (right - mid)//2
    r_value = math.floor(a*r/b) - a * math.floor(r/b)
    print(max, r_value)
    if max < r_value:
        left = mid
        continue
    #left
    l = left + (mid - left)//2
    l_value = math.floor(a*l/b) - a * math.floor(l/b)
    print(max, r_value)
    if max < l_value:
        right = mid
        continue

    if max >= l_value and max >= r_value:
        break



print(max)
