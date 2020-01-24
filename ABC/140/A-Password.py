a = int(input())
print(a*a*a)


def explore():
    #いけるノードを探す上下左右
    #探索済みであれば行かない
    #gGOALがあったらコストを１足して終了
    #行けたらコストをメモ
    #いけるノードがない場合はreturn
    #いけるノードがなくなったらFail
