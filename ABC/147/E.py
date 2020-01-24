H, W = map(int, input().split())
field_A = []
field_B = []

for i in range(H):
    field_A.append(list(map(int, input().split())))

for i in range(H):
    field_B.append(list(map(int, input().split())))

print(field_A)

red = []
blue = []

red.append(field_A[0][0])
blue.append(field_B[0][0])

dp = [][]

i = 0
j = 0


def isArea():
    if i >= 0 and i <= H-1 and j >=0 and j <= W-1:
        return True
    else:
        return False

while isArea():

    pass
