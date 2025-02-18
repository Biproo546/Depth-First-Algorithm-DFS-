def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    if start == target:
        print("\nTarget node found:", start)
        return True  

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True  

    return False 



graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}


target = 'I'
found = dfs(graph, 'S', target)

if not found:
    print(f"Target node '{target}' not found.")