"""
Task 7: Routing in a Web Server with a Trie

Complexity Analysis:
k = length of the path list.
TC: O(k)
SC: O(k)
"""


# A RouteTrieNode will be similar to our autocomplete TrieNode..
# with one additional element, a handler.
class RouteTrieNode:
    # Initialize the node with children as before, plus a handler
    def __init__(self):
        self.children = {}
        self.handler = None
        self.is_leaf = False

    # Insert the node as before
    def insert(self, sub_path):
        self.children[sub_path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler,
    # this is the root path or home page node
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.root.handler = handler

    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest)
    # node of this path
    def insert(self, path, handler):
        node = self.root

        for sub_path in path:
            if sub_path not in node.children:
                node.insert(sub_path)
            node = node.children[sub_path]

        node.handler = handler
        node.is_leaf = True

    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    def find(self, path):
        node = self.root

        for sub_path in path:
            if sub_path not in node.children:
                return None
            node = node.children[sub_path]

        if node.is_leaf:
            return node.handler
        else:
            return None


# The Router class will wrap the Trie and handle
class Router:
    # Create a new RouteTrie for holding our routes
    def __init__(self, handler):
        self.router = RouteTrie(handler)

    # Add a handler for a path
    # Path is a list created from splitting the input path_string
    def add_handler(self, path_string, handler):
        path = self._split_path(path_string)
        self.router.insert(path, handler)

    # Lookup path (by parts) and return the associated handler.
    # If path is empty, return the root handler.
    # If path is not empty, return the handler if specified.
    # If handler not found, return 404.
    # Path works with and without a trailing slash.
    # e.g. /about and /about/ both return the /about handler.
    # HTTP Code 200: OK, HTTP Code 404: Not found.
    def lookup(self, path_string):
        path = self._split_path(path_string)

        # Path is empty, return root handler.
        if path is None:
            code = 200
            handler = self.router.root.handler
            return code, handler

        # Look for the path in the router and return handler if exists.
        handler = self.router.find(path)
        if handler is not None:
            code = 200
            return code, handler

        # Handler not found, return 404
        code = 404
        handler = 'Page not found.'
        return code, handler

    # If the path has '/' at the beginning or ending, remove that.
    # Return an list after splitting the path_string by '/'
    def _split_path(self, path_string):
        if path_string.startswith('/'):
            path_string = path_string[1:]

        if path_string.endswith('/'):
            path_string = path_string[:-1]

        if len(path_string) == 0:
            return None

        return path_string.split('/')


# Here are some test cases and expected outputs
# you can use to test your implementation.

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/profiles/cristina-artist", "Hi! This is Christina.")


def test(router, path):
    response = router.lookup(path)
    print(f"Path: '{path}', Response: {response}")


# some lookups with the expected output

# Response: (200, 'root handler')
path = "/"
test(router, path)

# Response: (200, 'root handler')
path = ""
test(router, path)

# Response: (404, 'Page not found.')
path = "/home"
test(router, path)

# Response: (200, 'about handler')
path = "/home/about"
test(router, path)

# Response: (200, 'about handler')
path = "/home/about/"
test(router, path)

# Response: (404, 'Page not found.')
path = "/home/about/me"
test(router, path)

# Response: (200, 'Hi! This is Christina')
path = "/profiles/cristina-artist"
test(router, path)

# Response: (404, 'Page not found.')
path = "/profiles/james"
test(router, path)
