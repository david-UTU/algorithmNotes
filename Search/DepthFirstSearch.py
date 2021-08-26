#Good for graph/tree traversal
#Uses a stack to travere, meaning it goes to the first element added
vertices = ['0', '1', '2', '3', '4', '5', '6']
edges = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertices, edges)

def dfs(graph, start):
    vertices, edges = graph
    visits = []
    stack = [start]
    neighbors = [[] for vertex in vertices]

    for edge in edges:
        neighbors[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in neighbors[current]:
            if not neighbor in visits:
                stack.append(neighbor)
        visits.append(current)
    return visits

print(dfs(graphs, 0))