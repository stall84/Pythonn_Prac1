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
    print('Running the Depth First Traverse Iterative Function...')
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


# dft_iterative_printer(graph_adjacency_list, 'a')

print('-' * 40)
print('\n')
print('-' * 40)

counter = 0


def dft_recursive_printer(graph: dict, node: str) -> None:
    global counter
    if (counter == 0):
        print('Running the Depth First Traverse Recursive Function...')

    counter += 1
    # Utilize the python interpreters underlying call-stack instead of explicitly creating one
    # Do the  function's action
    print(node)
    # Set up the recursive 'driver' mechanism
    for neighbors in graph[node]:
        # Call yourself again, this time with the current node as the node argument
        dft_recursive_printer(graph, neighbors)


# dft_recursive_printer(graph_adjacency_list, 'a')


# Breadth-First-Traversal Functions.
# We'll utilize a queue-like structure with a List, removing the first-in element FIFO

def bft_iterative_printer(graph: dict, node: str) -> None:
    queue = [node]
    while (len(queue) > 0):
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


bft_iterative_printer(graph_adjacency_list, 'a')
