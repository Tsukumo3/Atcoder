N = int(input())
S = input()

grade_dict = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}
score = 0
for i in S:
    score += grade_dict[i]

print(score/N)
