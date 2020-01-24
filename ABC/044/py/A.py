import math

def is_prime(n):

    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    #print(n)

    #3から平方根まで２個ずつ飛ばしで計算する
    m = math.ceil(math.sqrt(n))
    for p in range(3,m+1,2):
        if n % p == 0:
            return False
    return True

def is_like_prime(n):
    #１のくらい

    n_str = str(n)

    if n_str[-1] == "5" or n%2 == 0:
        return False

    n_list = [int(i) for i in n_str]

    if sum(n_list)%3 == 0:
        return False

    return True

N = int(input())
#素数判定
ansFlag = is_prime(N)
#素数っぽい判定
if not ansFlag and not N == 1:
    ansFlag = is_like_prime(N)

if ansFlag:
    print("Prime")
else:
    print("Not Prime")
