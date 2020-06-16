# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # Initialize the trie with an root node and a handler,
    # this is the root path or home page node
    def __init__(self, ):
        pass

    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest)
    # node of this path
    def insert(self, ):
        pass

    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    def find(self, ):
        pass


# A RouteTrieNode will be similar to our autocomplete TrieNode..
# with one additional element, a handler.
class RouteTrieNode:
    # Initialize the node with children as before, plus a handler
    def __init__(self, ):
        pass

    # Insert the node as before
    def insert(self, ):
        pass


# The Router class will wrap the Trie and handle
class Router:
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    def __init__(self, ):
        pass

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
    def add_handler(self, ):
        pass

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
    def lookup(self, ):
        pass

    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    def split_path(self, ):
        pass


# Here are some test cases and expected outputs
# you can use to test your implementation.

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output

# should print 'root handler'
print(router.lookup("/"))

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))

# should print 'about handler'
print(router.lookup("/home/about"))

# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
