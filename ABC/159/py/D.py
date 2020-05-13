import collections

if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))

    c = collections.Counter(a)

    all = 0

    for item in c.items():
        all += item[1] * (item[1] - 1) //2

    for i in range(n):
        item = c[a[i]]
        after = item * (item-1) // 2
        before = (item-1) * (item-2) // 2
        #print(after, before)
        ans = all - after + before
        print(ans)
