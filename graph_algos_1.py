# Depth First Traversal Using Iterative Function

graph_adjacency_list = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': [],
    'e': ['b'],
    'f': ['d']
}


def dft_iterative_printer(graph: dict, origin: str) -> None:
    # Initiate the stack as a List
    stack = []
    # You could just place the origin param into the stack declaration above.
    stack.append(origin)
    # for node in stack:
    #     curr_node = stack[node]
    #     print(curr_node)\
    while len(stack):
        curr_node = stack.pop(-1)
        print(curr_node)
        for neighbor in graph[curr_node]:
            stack.append(neighbor)


dft_iterative_printer(graph_adjacency_list, 'a')
