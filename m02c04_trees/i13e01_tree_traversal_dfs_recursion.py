"""
Tree Traversal Logic
Visit: V
Left: L
Right: R

Pre-order traversal: VLR (V at the beginning)
In-order traversal: LVR (V in the middle)
Post-order traversal: LRV (V at last)
"""


# this code makes the tree that we'll traverse
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide whata print statement
    #   displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


"""
Pre-order traversal (VLR)
We want to visit the node, then traverse the left subtree,
and then traverse the right subtree
"""


def pre_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_value())

            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


print(f'Pre-order: {pre_order(tree)}')


"""
In-order traversal (LVR)
We want to traverse the left subtree, then visit the node,
and then traverse the right subtree.
"""


def in_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # visit node
            visit_order.append(node.get_value())

            # traverse right sub-tree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


# check solution: should get: ['dates', 'banana', 'apple', 'cherry']
print(f'In-order: {in_order(tree)}')


"""
Post-order traversal
Traverse left subtree, then right subtree,
and then visit the node.
"""


def post_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

            # visit node
            visit_order.append(node.get_value())

    traverse(tree.get_root())

    return visit_order


# check solution: should get: ['dates', 'banana', 'cherry', 'apple']
print(f'Post-order: {post_order(tree)}')
