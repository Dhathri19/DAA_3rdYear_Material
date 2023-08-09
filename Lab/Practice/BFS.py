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

def BFS(graph, starting_node, target_node):
    
    BFS_path = []
    
    visited_nodes = list()
    queue = Queue()
    
    queue.put(starting_node)
    visited_nodes.append(starting_node)
    
    while(not queue.empty()):
        
        current_node = queue.get()
        BFS_path.append(current_node)
        
        if(current_node == target_node):
            return BFS_path
            
        for neighbour_node in graph[current_node]:
            if(neighbour_node not in visited_nodes):
                queue.put(neighbour_node)
                visited_nodes.append(neighbour_node)

BFS_sNode = int(input("Enter the source node: "))
BFS_tNode = int(input("Enter the target node: "))

BFS_path = BFS(graph, BFS_sNode, BFS_tNode)
print(BFS_path)
