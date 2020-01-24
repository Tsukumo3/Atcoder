N = int(input())
S = input()

answers = [S[0]]

for i in S:
    if not i == answers[-1]:
        answers.append(i)

ans_str = "".join(answers)

ans = len(ans_str)

print(ans)
