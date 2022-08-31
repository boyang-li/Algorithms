# LeetCode 973. K Closest Points to Origin
#
# Complexity:
# Average case: O(n) time | O(n) space
# Worst case: O(n^2) time | O(n) space

from math import sqrt
from typing import List
import random

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = {}
    pointIndexes = [i for i in range(len(points))]
    for i in pointIndexes:
        distances[i] = sqrt(points[i][0] ** 2 + points[i][1] ** 2)

    print(distances)

    def swap(array, oneIdx, twoIdx):
        array[oneIdx], array[twoIdx] = array[twoIdx], array[oneIdx]

    def partition(lo, hi, pivot):
        pivotDistance = distances[pointIndexes[pivot]]
        print("partition begins: pointIndexes=", pointIndexes, " pivot=", pivot)

        # 1. move pivot to the end
        swap(pointIndexes, pivot, hi)

        # 2. move all points with less distances than pivot to the left
        storeIdx = lo
        for i in range(lo, hi):
            if distances[pointIndexes[i]] < pivotDistance:
                swap(pointIndexes, i, storeIdx)
                storeIdx += 1

        # 3. put pivot to its final sorted position
        swap(pointIndexes, hi, storeIdx)
        print(pointIndexes)
        return storeIdx

    def select(lo, hi, kSmallest):
        print("select begins: lo=", lo, " hi=", hi, " kSmallest=", kSmallest)
        if lo == hi:
            return

        pivotIdx = random.randint(lo, hi)
        print("lo= ", lo, " hi=", hi, " pivot=", pivotIdx)

        pivotIdx = partition(lo, hi, pivotIdx)

        print("pointIndexes=", pointIndexes, " sorted pivot=", pivotIdx)

        if kSmallest == pivotIdx:
            print("kSmallest == pivotIdx = ", pivotIdx)
            return
        elif kSmallest < pivotIdx:
            print("kSmallest < pivotIdx, go left", pivotIdx)
            return select(lo, pivotIdx - 1, kSmallest)
        else:
            print("kSmallest > pivotIdx, go right", pivotIdx)
            return select(pivotIdx + 1, hi, kSmallest)

    # kth smallest points' indexes are 0..k-1
    select(0, len(pointIndexes) - 1, k)

    print(pointIndexes)

    return [points[idx] for idx in pointIndexes[:k]]

def main():
    print(kClosest([[3, 3], [5, -1], [-2, 4]], 1))

if __name__ == "__main__":
    main()
