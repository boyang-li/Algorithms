# Brute-force approach
# Upper bound: O(nˆ2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):
    print("currentPermutation: ", currentPermutation, "permutations: ", permutations)
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(newArray, newPermutation, permutations)

# Optimal solution
# O(n*n!) time | O(n*n!) space
def getPermutations(array):
    perms = []
    permHelper(0, array, perms)
    return perms

def permHelper(i, array, perms):

    if i == len(array) - 1:
        # when i reaches the last index, take a snapshot of the permutation
        perms.append(array[:])
        print("appending to perms: ", perms)
    else:
        for j in range(i, len(array)):
            print("i: ", i, "j:", j, "array: ", array)
            swap(array, i, j)
            print("swap i and j:", array)
            permHelper(i + 1, array, perms)
            swap(array, i, j)
            print("swap i and j back:", array)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]