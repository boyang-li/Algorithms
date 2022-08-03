class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Notes:
    # In BFS, we iteratively explore all the child nodes of the current node
    # (using a queue/FIFO data structure) before we go deeper.
    #
    # Complexity:
    # Don't forget counting the edges of the graph when analyzing the time
    # comlexity of a graph traversing problem.
    # O(v + e) time | O(v) space
    # v = number of vertices; e = number of edges
    def bfs(self, array):
        # If we were permitted to use a list as if it was a queue
        queue = [self]
        # so long as the queue is not empty, continue the loop.
        while len(queue) > 0:
            # pop the first node off the queue.
            curr = queue.pop(0)
            # alway visit the node first
            array.append(curr.name)
            # push all of the child nodes of the current node to the queue.
            for child in curr.children:
                queue.append(child)

        return array
