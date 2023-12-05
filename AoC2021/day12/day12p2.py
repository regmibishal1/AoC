from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findPath(self):
        queue = []
        count = 0

        queue.append(['start'])
        while queue:
            path = queue.pop(0)
            prev = path[-1]

            for next in self.graph[prev]:
                repeated = next == next.lower() and next in path
                if next == 'end':
                    count += 1
                    continue
                if next == 'start' or path[0] == '*' and repeated:
                    continue
                queue.append((['*'] if repeated else []) + path + [next])
        print(count)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip().split('-') for line in lines]

    graph = Graph()
    for i in data:
        graph.addEdge(i[0], i[1])
        graph.addEdge(i[1], i[0])
    graph.findPath()
