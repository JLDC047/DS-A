class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = [[] for i in range(0, n)]

    def create_edge(self, node1, node2): 
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)  

    def bfs(self, source):
        visited = []
        queue = [] 
        distance = [0 for i in range(0, self.nodes)]

        queue.append(source) 
        visited.append(source) 

        while len(queue) > 0:
            current = queue.pop(0)
            for node in self.edges[current]:
                if node not in visited:
                    queue.append(node)
                    visited.append(node)
                    distance[node] = distance[current] + 1

        return visited, distance
    
graph = Graph(8)
graph.create_edge(0,1)
graph.create_edge(0,2)
graph.create_edge(0,3)
graph.create_edge(1,4)
graph.create_edge(2,3)
graph.create_edge(2,5)
graph.create_edge(3,5)
graph.create_edge(5,6)
graph.create_edge(4,7)
graph.create_edge(5,7)


bfs, distance = graph.bfs(5)
print(bfs)
print(distance)

