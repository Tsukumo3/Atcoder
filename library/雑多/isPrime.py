import math

def is_prime(n):
    '''素数判定をする
    '''
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def is_prime_list(n):
    '''素数のリスト
    '''
    if n == 1: return False
    ans = []
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            ans.append(k)
    return ans

def is_prime_number(n):
    '''素数のリスト
    '''
    if n == 1: return False
    ans = 0
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            ans += 1
    return ans
