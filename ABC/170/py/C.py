x, n = map(int, input().split())
if n == 0:
    print(x)
else:
    p = list(map(int, input().split()))

    check = [True]*10001

    for i in p:
        check[i] = False

    mini = 100000
    index = 1

    for i in range(0,1001):
        if check[i]:
            if mini > abs(x-i):
                #print(mini, abs(x-i), i)
                mini = abs(x-i)
                index = i

    #マイナス
    for i in range(1,1001):
        if mini >= abs(x+i):
            #print(mini, abs(x+i), -i)
            mini = abs(x+i)
            index = -i

    print(index)
