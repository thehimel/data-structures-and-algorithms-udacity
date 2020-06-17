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
"""


class Graph:
    def __init__(self):
        self.nodes = set()
        self.friends = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.friends[from_node].append(to_node)
        self.friends[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

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

    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited:
        best_friend = None

        # 1. Find the unvisited node having smallest known distance
        # from the source node.
        for node in unvisited:
            if best_friend is None:
                best_friend = node
            elif output[node] < output[best_friend]:
                best_friend = node

        # known distance of best_friend
        best_distance = output[best_friend]

        # 2. For the current node, find all the unvisited friends.
        # Calculate the distance of each unvisited friend.
        for friend in graph.friends[best_friend]:
            if friend in unvisited:
                distance = best_distance + graph.distances[(
                    best_friend, friend)]

                # 3. If the calculated distance of the unvisited friend is
                # less than the already known distance in output dictionary,
                # update the shortest distance in the output dictionary.
                if distance < output[friend]:
                    output[friend] = distance

                    # 4. If there is an update in the output dictionary,
                    # update the path dictionary as well for the same key.
                    path[friend] = best_friend

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(best_friend)

    return output


# Test 1
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    graph.add_node(node)

graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 6)
graph.add_edge('B', 'C', 1)
graph.add_edge('C', 'E', 2)
graph.add_edge('E', 'D', 1)

graph.print_graph()

# {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}
print(dijkstra(graph, 'A'))

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

# {'A': 0, 'B': 5, 'C': 10}
print(dijkstra(graph, 'A'))

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

# {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
print(dijkstra(graph, 'A'))
