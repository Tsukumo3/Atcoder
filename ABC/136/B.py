input_string = input()
length = len(input_string)
n = int(input_string)

ans = 0

def func(i):
    a = '9'*i
    b = '1' + '0'*(i-1)
    A = int(a)
    B = int(b)

    if A > n:
        A = n

    return A - B + 1

ans = n
for i in range(0, length+1, 2):
    if i == 0:
        continue
    ans -= func(i)
print(ans)
