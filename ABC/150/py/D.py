def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers, N):

    ans = numbers[0]

    for i in range(1,N):
        ans = lcm_base(ans,numbers[i])

    return ans

N ,M = map(int, input().split())
A_n = list(map(int,input().split()))



a_lcm = lcm_list(A_n,N)
ans = 0
interval = a_lcm//2

amari = M // interval

if amari%2 == 1:
    amari = (amari+1)//2
else:
    amari = amari//2
print(amari)
