n = int(input())

class student:
    def __init__(self, number, name):
        self.number = number
        self.name = name

a = list(map(int, input().split()))
order = []
for i in range(n):
    order.append(student(a[i],i+1))

reorder = sorted(order, key=lambda u: u.number)

for i in range(n):
    if i == n-1:
        print(reorder[i].name)
    else:
        print(reorder[i].name, end=" ")
