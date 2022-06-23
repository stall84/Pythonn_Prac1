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


# bft_iterative_printer(graph_adjacency_list, 'a')

# Map an undirected graph's edge-list (eL: [[nodes]]) to an adjacency list (aL: {node: [neighbors]})

edge_list = [
    ['i', 'j'],
    ['k', 'i'],
    ['j', 'k'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def graph_map(edgeList: list[str, str]) -> dict:
    graph = {}
    for edge in edgeList:
        [a, b] = edge
        if not (a in graph):
            graph[a] = []
        if not (b in graph):
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


mapd_graph = graph_map(edge_list)
print('mapd_graph : ', mapd_graph)

# Working with un-directed graphs still, we want to write our traversal algorithms again, but this time
# we need to guard against getting stuck in a cycle.
# The way we'll do this is by marking each node we visit as visited, and using logic to not attempt to re-visit
# already-visited nodes


# def cycle_guarded_dft(graph: any, source: str) -> None:
#     stack = [source]
#     visited =
#     current = stack.pop(-1)
#     for neighbor in graph[current]:
