'''
n = int(input())
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [int(input()) for i in range n]
p = [list(map(int, input().split()))]

a = input()
a, b = input().split()
a = [input() for i in range n]
'''
n, k = map(int, input().split())

########関数部分##############
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
############################


#####関数をつかってみる．#####
x2 = Base_10_to_n(n, k)
print(len(x2))#"100011"が表示される．
