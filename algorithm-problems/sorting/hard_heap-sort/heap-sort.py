# Notes:
# The Heap Sort slgorithm involves building a Max Heap. A Max Heap is essentialy
# a binary tree with the following properties:
# - It is complete: all levels are filled up except the last level which is
# filled up from left to right.
#
# - the heap proerty: for Max Heap, every node's value is greater than or equal
# to its children.
#
# Now the critical part of the algorithms is this: we setup a loop to
# iterate the heap array in reverse order, and we essentailly separate the
# array into two part. The first subarray is the heap we maintain, and the
# second subarray is the sorted array.
#
# Complexity:
# Building heap runs in linear time, but siftDown runs in O(log(n)) time and we
# run it n times. For space, we only swap elements and we do it in place.
# O(nlog(n)) time | O(1) space
def heapSort(array):
    # first, we build a Max Heap from the input array
    buildMaxHeap(array)
    #
    for endIdx in reversed(range(1, len(array))):
        # swap the root node of the heap with the last node of the heap, the
        # root node will always be the largest node of the heap subarray, and by
        # swapping it to the last node of the heap, it is now in sorted order in
        # the second subarray.
        swap(0, endIdx, array)
        # we run sift down on the new root node to maintain the heap, only
        # except the heap we pass in this time does not include the last node
        # which was the root node we swapped. when we finish the loop, the array
        # will be sorted.
        siftDown(0, endIdx - 1, array)
    return array

# This function build a Max Heap for the given array in place
def buildMaxHeap(array):
    # locate the first parent from the bottom of the heap, which would be the
    # furthest parent in the array representation of the heap.
    firstParentIdx = (len(array) - 1) // 2
    # loop the heap array backwards, and start to sift nodes down beginning at
    # the first parent node
    for currIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currIdx, len(array) - 1, array)

# This function sift a node down in a Max Heap
def siftDown(currIdx, endIdx, heap):
    # locate the first child node by applying the formula: 2*i + 1
    childOneIdx = currIdx * 2 + 1
    # So long as the first child node is in bound, continue the loop
    while childOneIdx <= endIdx:
        # try to locate the second child node by applying the formula:
        # 2*i + 2, set it to -1 if out of bound
        childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
        # find the child with larger value the node to swap with the parent
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        # if the child to swap has a larger value than the parent, swap them and
        # update the child to become the new current parent
        if heap[idxToSwap] > heap[currIdx]:
            swap(currIdx, idxToSwap, heap)
            currIdx = idxToSwap
            childOneIdx = currIdx * 2 + 1
        else:
            return

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
