class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Notes:
    # In DFS, we recursively explore the child nodes until there are no
    # child nodes left.
    #
    # Complexity:
    # O(v + e) time | O(v) space - where v is the number of viertices/nodes, and
    # e is the number of edges.
    def depthFirstSearch(self, array):
        # always add the node's name to the output array first
        array.append(self.name)

        # iterate through the children node list, and recursively call
        # DFS function on each children nodes
        for child in array.children:
            child.depthFirstSearch(array)

        return array
