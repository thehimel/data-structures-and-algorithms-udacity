"""
Graph Depth First Search Recursive Solution

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
def dfs_search(start_node, search_value):
    visited = set()               # Set to keep track of visited nodes.
    return dfs(start_node, visited, search_value)


# Recursive function
def dfs(node, visited, search_value):
    if node.value == search_value:
        return node

    visited.add(node)
    result = None

    # Conditional recurse on each neighbour
    for child in node.children:
        if (child not in visited):
            result = dfs(child, visited, search_value)

    return result


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
