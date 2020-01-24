div = 10**9 + 7
ans = 0

N = int(input())
A = list(map(int, input().split()))

#最大値
A_max = max(A)
#最大値を２進数化
A_max_bin = format(A_max, 'b')
#その桁数
max_digits = len(A_max_bin)

#print(max_digits)

input_format = '0' + str(max_digits) + 'b'

A_bin = [ format(item,input_format) for item in A]

#print(A_bin)

ans = 0

for i in range(1,max_digits+1):
    num0 = 0
    num1 = 0
    #print("桁数 : " + str(i))
    for A_i in A_bin:

        #print(str(A_i) + " : " + str(A_i[-i]))
        #i桁目が0だったら

        #print(type(A_i[-1]))

        if A_i[-i] == '0':
            num0 += 1
        else:
            num1 += 1

    ans += num0 * num1 * 2**(i-1)
    #print(ans)

    num0 = 0
    num1 = 0

#print(ans)


print(ans%div)
