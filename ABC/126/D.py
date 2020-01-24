class Node:
    def __init__(self,n):
        self.name = n
        self.parents = []
        self.children = []
        self.color = 0




def main():
    N = int(input())
    lines = [list(map(int, input().split())) for i in range(N-1)]

    nodes = [Node(i) for i in range(1,N+1)]

    for line in lines:
        parent = line[0]
        child = line[1]

        nodes[parent-1].children.append(nodes[child-1])
        nodes[child-1].parents.append(nodes[parent-1])

    maxColor = 0
    for node in nodes:

        print(node.name)
        print(len(node.parents))
        print(len(node.children))
        print("")

        if maxColor < len(node.children):
            maxColor = len(node.children)

    print(maxColor)

if __name__ == '__main__':
    main()
