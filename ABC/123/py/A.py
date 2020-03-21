cities = [int(input()) for i in range(5)]
k = int(input())

for i in range(4):
    for j in range(i+1, 5):
        #print(i, j)
        if abs(cities[i] - cities[j]) > k:
            print(":(")
            exit()
else:
    print("Yay!")
