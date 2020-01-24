n = int(input())

book = []

for i in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    number = i+1
    list = [name,score,number]
    book.append(list)

#sort
'''
book.sort(key=lambda x: x[n])でソート
-マイナス指定している・・・
'''
book.sort(key=lambda x: (x[0], -x[1]))
print("")
[print(item[2]) for item in book]
