N = int(input())
Card_n = list(map(int, input().split()))

Card_n.sort()

A_n = []
B_n = []

for i in range(len(Card_n)):
    if not i%2 == 0:
        A_n.append(Card_n.pop())
    else:
        B_n.append(Card_n.pop())

#print(A_n)
#print(B_n)
print(abs(sum(A_n) - sum(B_n)))
