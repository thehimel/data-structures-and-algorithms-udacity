# Helper Code
import sys
from collections import defaultdict


"""
class Graph:
__init__():
    - nodes: A set cannot contain duplicate nodes
    - friends: Defaultdict is a child class of Dictionary that provides
    a default value for a key that does not exists.
    - distances: Dictionary. An example record as ('A', 'B'): 6
    shows the distance between 'A' to 'B' is 6 units

add_edge(): Graph undirected / bidirectional

Algorithm (Greedy Approach):
1. Find the unvisited node having smallest known distance from the source node.

2. For the current node, find all the unvisited friends. Calculate the
distance of each unvisited friend.

3. If the calculated distance of the unvisited friend is less than the already
known distance in output dictionary, update the shortest distance in the
output dictionary.

4. If there is an update in the output dictionary, means the best_friend is
updated. Thus, update best_friends dictionary.

5. Remove the current node from the unvisited set.

Note: The numbers of the algorithm are associated with the # numbers
in the code. Match the numbers with the code to get detailed information.
"""


class Graph:
    def __init__(self):
        self.nodes = set()
        self.friends = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, from_node, to_node, distance):
        self.friends[from_node].append(to_node)
        self.friends[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def add_edges(self, edges):
        for (from_node, to_node) in edges:
            distance = edges[(from_node, to_node)]
            self.add_edge(from_node, to_node, distance)

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Friends are: ", self.friends)
        print("Distances are: ", self.distances)


# Find the shortest path from the source node to every other node in the graph
def dijkstra(graph, source):

    output = {}
    output[source] = 0

    for node in graph.nodes:
        if (node != source):
            output[node] = sys.maxsize

    unvisited = set(graph.nodes)

    best_friends = {}

    # As long as unvisited is non-empty
    while unvisited:
        best_friend = None

        # 1
        for node in unvisited:
            if best_friend is None:
                best_friend = node
            elif output[node] < output[best_friend]:
                best_friend = node

        # Known distance of best_friend
        best_distance = output[best_friend]

        # 2
        for friend in graph.friends[best_friend]:
            if friend in unvisited:
                distance = best_distance + graph.distances[(
                    best_friend, friend)]

                # 3
                if distance < output[friend]:
                    output[friend] = distance

                    # 4
                    best_friends[friend] = best_friend

        # 5
        unvisited.remove(best_friend)

    return output


def create_graph(nodes, edges):
    graph = Graph()
    graph.add_nodes(nodes)
    graph.add_edges(edges)
    return graph


def test(graph, source):
    output = dijkstra(graph, source)
    # print(output)
    for friend in output:
        print(f'{source}->{friend}={output[friend]}', end=' | ')
    print()


# Test 1
nodes = ['A', 'B', 'C', 'D', 'E']
edges = {
    ('A', 'B'): 3, ('A', 'D'): 2, ('B', 'D'): 4, ('B', 'E'): 6,
    ('B', 'C'): 1, ('C', 'E'): 2, ('E', 'D'): 1
}
graph = create_graph(nodes, edges)
# graph.print_graph()

# {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}
test(graph, 'A')

# Test 2
nodes = ['A', 'B', 'C']
edges = {
    ('A', 'B'): 5, ('B', 'C'): 5, ('A', 'C'): 10
}
graph = create_graph(nodes, edges)

# {'A': 0, 'B': 5, 'C': 10}
test(graph, 'A')

# Test 3
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = {
    ('A', 'B'): 5, ('A', 'C'): 4, ('D', 'C'): 1, ('B', 'C'): 2,
    ('A', 'D'): 2, ('B', 'F'): 2, ('C', 'F'): 3, ('E', 'F'): 2,
    ('C', 'E'): 1
}
graph = create_graph(nodes, edges)

# {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
test(graph, 'A')
test(graph, 'B')
