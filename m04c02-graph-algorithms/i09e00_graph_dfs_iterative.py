"""
Graph Depth First Search
To start, create a graph class in Python.
Then create the graph.

Implement DFS
Using what you know about DFS for trees, apply this to graphs.
Implement the dfs_search to return the GraphNode with the value target
starting at the root_node.
"""


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, target):
        if target in self.children:
            self.children.remove(target)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


# Solution
def dfs_search(root_node, target):
    visited = set()                         # Sets are faster for lookups
    stack = [root_node]                     # Start with a given root node

    while len(stack) > 0:                   # Repeat until the stack is empty

        current_node = stack.pop()          # Pop out a node added recently
        visited.add(current_node)           # Mark it as visited

        if current_node.value == target:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before,
            # and not available in the stack already.
            if (child not in visited) and (child not in stack):
                stack.append(child)


# Tests
assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')
print('All tests passed.')
