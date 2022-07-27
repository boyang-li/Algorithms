# Notes:
# A min/max heap is basically a binary tree, and it satisfies the below
# properties:
# - It is complete: all its levels are filled up except the last level which is
# filled up from left to right.
#
# - the heap proerty: for Min Heap, every node's value is smaller than or equal
# to its children. Vice-versa for the Max Heap.
#
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # For a given array of numbers, build a Min Heap in place. We locate the
    # first parent by applying the formula on the final index of the heap:
    #     parent_index = floor((current_index - 1) / 2)
    # from there to the very top of the heap, we sift down every node, and we
    # finish building the Min Heap when we are done.
    #
    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 1 - 1) // 2
        for currIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currIdx, len(array) - 1, array)
        return array

    # This function sifts the current node down in the Min Heap. We first find
    # the child nodes(could have 1 or 2 child node, if no child node found we
    # have reached the bottom of the heap and we are done), we find the child
    # nodes' indices by applying the formula:
    #     first_child_index = 2 * i + 1; second_child_index = 2 * i + 2
    # then we find the smaller child node, and swap it with the current node if
    # it is STRICTLY SMALLER than the current node.
    #
    # O(log(n)) time | O(1) space
    def siftDown(self, currIdx, endIdx, heap):
        # locate the first child node.
        childOneIdx = currIdx * 2 + 1
        while childOneIdx <= endIdx: # if we are still in bound of the heap
            # locate the second child node if it exists.
            childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
            # locate the minimum node between the child nodes.
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            # swap the current node with the child node if the child node is
            # strictly smaller, then increment the indices of current node and
            # first child node for loop the continue. Otherwise, we are done.
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                childOneIdx = currIdx * 2 + 1
            else:
                return

    # This function sifts the current node up in the Min Heap. We first find the
    # current node's parent index by applying the formula:
    #     parent_index = floor((current_index - 1) / 2)
    # then keep swapping the current node with the parent as long as they are
    # out of positions.
    #
    # Complexity:
    # O(log(n)) time | O(1) space
    def siftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # To remove a value from the heap, we first swap the current root node with
    # the last node in the heap, pop the last node(the node we are removing),
    # and sift the root node down.
    #
    # Complexity:
    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # To insert a value to the heap, simply append the value at the end of heap,
    # and then sift the node up.
    #
    # Complexity:
    # O(log(n)) time | O(1) space
    def insert(self, value):
        # append the value to the end of the heap
        self.heap.append(value)
        # sift the last value up by passing in the last index of the heap
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
