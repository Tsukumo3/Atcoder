import collections

k = int(input())
time = 1

q = collections.deque()

q.extend([1,2,3,4,5,6,7,8,9])

while(time <= k):

    i = q.popleft()
    #print(i)
    time += 1

    #0じゃないなら
    if i % 10 != 0:
        q.append(i*10 + i%10 - 1)

    #それ以外
    q.append(i*10 + i%10)

    #9じゃないなら
    if i % 10 != 9:
        q.append(i*10 + i%10 + 1)

print(i)
