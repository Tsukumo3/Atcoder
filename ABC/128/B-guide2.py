'''
ソートのリストの仕組みを考えると
リストを全部ソートしかない

同じ名前で一つのリストにすることができれば昇順で並べ替えれる



とりあえずソートして
同じ名前をまとめていくことで実現可能

    前からデータの最初のnameを取り出し同じであればリストに追加していく

データ構造としては

[ [kazan 35] [kazan 50] ]
[ [khabarovsk 40] [khabarovsk 20]]
[ [moscow 10] [moscow 60] ]
上と名前でまとめた結果のリストとする



'''
n = int(input())

book = []

for i in range(n):
    line = input().split()
    name = line[0]
    score = 100 - int(line[1])
    number = i+1
    list = [name,score,number]
    book.append(list)

#ソート
sorted_book = sorted(book)
print("")
[print(i) for i in sorted_book]

#名前でまとめた結果のリスト
nameList = []
nameList.append([])
nameList[0].append(sorted_book[0])

for i in range(1,len(sorted_book)):

    if sorted_book[i-1][0] == sorted_book[i][0]:
        nameSet.append(sorted_book[i])
    else:
        print(nameSet)
        nameList.append(nameSet)
        nameSet.append(sorted_book[i])
nameList.append(nameSet)

#再度全体でソートをかけると
sorted_book2 = sorted(nameList)
print("")
[print(i) for i in sorted_book2]
