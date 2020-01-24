A,B,C,D = map(int, input().split())

def gcd(a, b):
    while b: a, b = b, a % b
    return a

 #最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

#Bで割り切れれない数 = B - Bで割り切れる数
_not_Divisible_number_B = B - (B//C + B//D - B//lcm(C,D))

#A以上B以下なので
lowA =  A -1

_not_Divisible_number_A_1 = lowA - (lowA//C + lowA//D - lowA//lcm(C,D))

ans = _not_Divisible_number_B - _not_Divisible_number_A_1

print(ans)
