if __name__ == '__main__':
    n, m = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(m)]

    rank = [-1] * n

    for i in l:
        
