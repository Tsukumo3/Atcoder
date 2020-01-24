# -*- coding:utf-8 -*-
# A.py : A - Round One

def main():
    _a = int(input())
    _b = int(input())

    answers = [1,2,3]

    _a_index = answers.index(_a)
    answers.pop(_a_index)

    _b_index = answers.index(_b)
    answers.pop(_b_index)

    print(answers[0])

if __name__ == '__main__':
    main()
