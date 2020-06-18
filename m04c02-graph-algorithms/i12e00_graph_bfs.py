"""
Graph Breadth First Search
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
def bfs_search(root_node, search_value):
    visited = set()  # Sets are faster while lookup.
    queue = [root_node]  # Lists are faster to iterate.

    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)


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
assert nodeA == bfs_search(nodeG, 'A')
assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')

assert None is bfs_search(nodeG, 'X')
print('All tests passed.')
