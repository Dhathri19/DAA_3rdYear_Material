from queue import Queue

graph = {
            5 : [3, 7],
            3 : [2, 4],
            7 : [8, 9],
            2 : [10],
            4 : [8],
            8 : [],
            9 : [],
            10 : []
        }

def DFS(graph, starting_node, target_node, path, visited = []):
    path.append(starting_node)
    visited.append(starting_node)
    if starting_node == target_node:
        return path
    for neighbour_node in graph[starting_node]:
        if neighbour_node not in visited:
            result = DFS(graph, neighbour_node, target_node, path, visited)
            if result is not None:
                return result
    path.pop()
    return None

DFS_path = []
DFS_sNode = int(input("Enter the source node: "))
DFS_tNode = int(input("Enter the target node: "))
DFS_path = DFS(graph, DFS_sNode, DFS_tNode, DFS_path)
print(DFS_path)