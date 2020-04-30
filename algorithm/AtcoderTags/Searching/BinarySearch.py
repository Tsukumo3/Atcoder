'''
二分探索アルゴリズム

単純な線形探索は O(n)
二分探索なら 0(log n)

'''

# *************************************

'''
1. ソート済みの配列の中から目的のものを探す　
数あるときはどれになるかわからない。
'''
"""
a = [1, 14, 32, 51, 51, 51, 288, 299, 500, 910, 10000, 10930]

def binary_search(key):
    '''
    目的の値 key の index を返すようにする。ない場合は -1
    '''
    left = 0
    right = len(a) - 1

    while(left <= right):
        mid = (left + right)//2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            left = mid + 1
        elif a[mid] > key:
            right = mid - 1
    return -1

if __name__ == '__main__':
    print(binary_search(51))
    print(binary_search(1))
    print(binary_search(288))
    print(binary_search(999))
: output
5
0
6
-1
"""

# *************************************

'''
1.2 最小のindexを返す。

std::lower_bound()は
iterator の key以上となる最小のindexを返す。

・key がなくても key が a の中で何番目に小さいかわかる
・複数の key がある場合は、最小のものを選ぶ

一般化する
'''

# *************************************

'''
2. 一般化した二分探索法

いわゆる巡る式二分探索

left 常に　条件を満たさない
right 常に　条件を満たす
最終的には条件を満たす
最も大きい条件を満たさない値のleft
最も小さい条件を満たす値のraigt
right - left = 1となるようにする
overflowを防いでいる。

最も小さいindexを探す

'''

# *************************************

"""
a = [1, 14, 32, 51, 51, 51, 288, 299, 500, 910, 10000, 10930]

def isOK(mid, key):
    if a[mid] >= key:
        return True
    else:
        return False

def binary_search(key):
    '''
    目的の値 key の index を返すようにする。ない場合は最も小さいindexを返す。
    '''
    left = -1 # 0が条件を満たすこともある
    right = len(a) # 最後が条件を満たすこともある

    while(right - left > 1):

        mid = left + (right - left)//2

        if isOK(mid, key):
            right = mid
        else:
            left = mid

    # 右側が条件を満たさないのであれば、rightが条件を満たす最小になる
    return right

if __name__ == '__main__':
    print(binary_search(51))
    print(binary_search(1))
    print(binary_search(288))
    print(binary_search(999))
#3
#0
#6
#10
"""

# *************************************

'''
2.2 一般化した二分探索法

いわゆる巡る式二分探索

条件を満たす最も大きいindexを探す

: left right どっちが大きいか　51 51を比較する必要がある。

'''

# *************************************

a = [1, 14, 32, 51, 51, 51, 288, 299, 500, 910, 10000, 10930]

def isOK(mid, key):
    if a[mid] >= key:
        return True
    else:
        return False

def binary_search(key):
    '''
    目的の値 key の index を返すようにする。ない場合は最も大きいindexを返す。
    3
    0
    6
    10
    '''
    ng = -1 # 0が条件を満たすこともある
    ok = len(a) # 最後が条件を満たすこともある

    # ok と ng のどちらが大きいか分からないことを考慮
    while(abs(ok - ng) > 1):
        mid = (ok + ng)//2
        if isOK(mid, key):
            ok = mid
        else:
            ng = mid

    # 右側が条件を満たさないのであれば、rightが条件を満たす最小になる
    return ok

if __name__ == '__main__':
    print(binary_search(51))
    print(binary_search(1))
    print(binary_search(288))
    print(binary_search(999))

# *************************************
