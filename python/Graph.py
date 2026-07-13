# #Adjacency List
# graph = {
# "A":["B","C"],
# "B":["A","c","D"],
# "c":["A","B"],
# "D":["B"]
# }
# print(graph)

# #Creating a Graph in Python
# graph = {}
# graph["A"] = ["B","C"]
# graph["B"] = ["A"]
# graph["C"] = ["A"]
# print(graph)

# #Adding a Node
# graph = {}
# graph["A"] = []
# graph["B"] = []
# print(graph)

# #Adding an Edge
# graph["A"].append("B")
# graph["B"].append("A")
# print(graph)

# #Traversing a Graph
# #1. DFS (Depth First Search)/Recursive

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": [], "D": [], "E": []}
visited = set()


def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)


dfs("A")

# 2. BFS (Breadth First Search)
