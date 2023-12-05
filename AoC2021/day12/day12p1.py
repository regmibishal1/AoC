from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findPath(self, s, d):
        visited = {vert: False for vert in self.graph}
        path = []
        count = [0]
        self.findPathRec(s, d, visited, path, count)
        print(count[0])

    def findPathRec(self, u, d, visited, path, count):
        visited[u] = True
        if u == u.upper():
            allSet = True
            for vert in self.graph[u]:
                if not visited[vert]:
                    allSet = False
            visited[u] = allSet

        path.append(u)

        if u == d:
            count[0] += 1
            print(path)
        else:
            for vert in self.graph[u]:
                if not visited[vert]:
                    self.findPathRec(vert, d, visited, path, count)
        path.pop()
        visited[u] = False


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip().split('-') for line in lines]

    graph = Graph()
    for i in data:
        graph.addEdge(i[0], i[1])
        graph.addEdge(i[1], i[0])
    graph.findPath('start', 'end')
