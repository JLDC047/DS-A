class Graph:
    def __init__(self, n):
        self.nodes = n
        self.edges = [[] for i in range(0, n)]

    def create_edge(self, node1, node2): 
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

    def dfs(self, source):
        visited = []
        stack = []

        stack.append(source)

        while len(stack) > 0:
            current = stack.pop(-1)
            print(current, "is current")
            visited.append(current)
            print(visited, "is visited")
            print(self.edges[current], "are edges of current")
            for node in self.edges[current]:
                if node not in visited and node not in stack:
                    stack.append(node)
            print(stack, "is stack")        

        return visited

"""graph = Graph(8)
graph.create_edge(0,1)  
graph.create_edge(0,2) 
graph.create_edge(0,7) 
graph.create_edge(1,2)  
graph.create_edge(1,4)  
graph.create_edge(2,3)    
graph.create_edge(2,4)
graph.create_edge(2,5)
graph.create_edge(2,6)
graph.create_edge(2,7)     
graph.create_edge(3,4) 
graph.create_edge(3,6)
graph.create_edge(5,6) 
graph.create_edge(5,7)""" 

graph = Graph(5)
graph.create_edge(0,1)
graph.create_edge(0,2)
graph.create_edge(0,3)
graph.create_edge(1,4)
graph.create_edge(2,3)

print(graph.dfs(0))    

