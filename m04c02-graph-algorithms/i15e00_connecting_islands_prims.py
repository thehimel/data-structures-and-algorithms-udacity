"""
param: num_islands - number of islands
param: bridge_config - bridge configuration
return: cost (int) minimum cost of connecting all islands
"""
# Solution

# The following Solution makes use of one of Python's PriorityQueue (heapq)
# Details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq


# Helper function to create graph using adjacency list implementation
def create_graph(num_islands, bridge_config):
    # A graph can be represented as a adjacency_list,
    # which is a list of blank lists
    graph = [list() for _ in range(num_islands + 1)]

    # populate the adjacency_list
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]

        # An entry in a sublist of graph is represented
        # as a tuple (friend, cost)
        graph[source].append((destination, cost))
        graph[destination].append((source, cost))

    # print("graph = ", graph)
    return graph


# Function to find minimum cost of connecting all islands
def minimum_cost(graph):
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # Heap is represented as a list of tuples
    # A "node" in heap is represented as tuple (cost, friend)
    min_heap = [(0, start_vertex)]
    total_cost = 0

    while len(min_heap) > 0:
        # Here, heapq.heappop() will automatically pop out the "node" having
        # smallest cost, and reduce the heap size
        cost, current_vertex = heapq.heappop(min_heap)

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total_cost
        total_cost += cost

        for friend, cost in graph[current_vertex]:
            heapq.heappush(min_heap, (cost, friend))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


"""
(1) --- 1 --- (2)
 |\\           |
 3   ` 10      4
 |        ` \\ |
(4) --- 2 --- (3)
"""
# bridge_config: [[island_1, island_2, cost_1], [island_2, island_3, cost_4]..]
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
