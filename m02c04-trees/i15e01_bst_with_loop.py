"""
Time Complexities:
Search, Insertion, Deletion: O(log(n))
"""


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
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    # Insertion
    def insert(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node is None:
            self.root = new_node
            return

        while(True):
            if new_node.get_value() == node.get_value():
                node.set_value(new_node.get_value())
                break

            elif new_node.get_value() < node.get_value():
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break

            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

    # Search
    def search(self, value):
        node = self.get_root()
        s_node = Node(value)
        while(True):
            if s_node.get_value() == node.get_value():
                return True

            elif s_node.get_value() < node.get_value():
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False

            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False


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


tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
# insert duplicate
tree.insert(5)

print(pre_order(tree))
print(tree.search(4))
print(tree.search(8))
