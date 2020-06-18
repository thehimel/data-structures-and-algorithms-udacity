"""
Graph Depth First Search
To start, create a graph class in Python.
Then create the graph.

Implement DFS
Using what you know about DFS for trees, apply this to graphs.
Implement the dfs_search to return the GraphNode with the value target
starting at the root_node.

Note: To visualize the algorithms, first convert the graph to a tree like
graph with the adjacency list and then go along the algorithm in paper.
"""


class GraphNode(object):
    def __init__(self, value):
        self.value = value
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

    def adjacency_list(self):
        output = list()

        for node in self.nodes:
            children = [child.value for child in node.children]
            output.append(children)

        return output


# Solution
def dfs_search(root_node, target):
    visited = set()  # Sets are faster for lookups

    stack = list()
    stack.append(root_node)  # Start with a given root node

    while len(stack) > 0:                   # Repeat until the stack is empty
        current_node = stack.pop()          # Pop out a node added recently
        visited.add(current_node)           # Mark it as visited

        if current_node.value == target:
            return current_node

        # Check all the children. If a node hasn't been visited yet,
        # and not available in the stack already, push it in the stack.
        for child in current_node.children:
            if (child not in visited) and (child not in stack):
                stack.append(child)

    return None  # If not found


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

node_list = [nodeG, nodeR, nodeA, nodeP, nodeH, nodeS]
graph = Graph(node_list)
graph.add_edge(nodeG, nodeR)
graph.add_edge(nodeA, nodeR)
graph.add_edge(nodeA, nodeG)
graph.add_edge(nodeR, nodeP)
graph.add_edge(nodeH, nodeG)
graph.add_edge(nodeH, nodeP)
graph.add_edge(nodeS, nodeR)

print(graph.adjacency_list())

# Tests
assert nodeA == dfs_search(nodeG, 'A')
assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')

assert None is dfs_search(nodeG, 'X')
print('All tests passed.')

"""
     G
   / | \
 /   |   \
H    A -- R
|       / |
|     /   |
|   /     |
| /       |
P         S
"""
