from fractions import Fraction

if __name__ == '__main__':
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]

    L = {}
    R = {}

    for i in l:
        L[Fraction(i[0]/i[1])] Fraction(i[0]/i[1])

        R.append(Fraction(-i[1]/i[0]))
