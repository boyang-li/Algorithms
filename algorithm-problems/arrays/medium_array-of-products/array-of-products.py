# Brute-force
# O(nˆ2) time | O(n) - where n is the length of the input array
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]

  for i in range(len(array)):
    runningProduct = 1
    for j in range((len(array))):
      if i != j:
        runningProduct *= array[j]
    products[i] = runningProduct

  return products

# Optimal solution
# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]
  leftProducts = [1 for _ in range(len(array))]
  rightProducts = [1 for _ in range(len(array))]

  leftRunningProduct = 1
  for i in range(len(array)):
    leftProducts[i] = leftRunningProduct
    leftRunningProduct *= array[i]

  rightRunningProduct = 1
  for i in reversed(range(len(array))):
    rightProducts[i] = rightRunningProduct
    rightRunningProduct *= array[i]

  for i in range(len(array)):
    products[i] = leftProducts[i] * rightProducts[i]

  return products

# Notes:
# A clever optimal solution solves it by having a single forward loop to
# calculate the running products of all the elements to the left up until the
# current index, and then having a single backward loop to calculate the running
# products of all the elements to the right up until the current index.
#
# Note that the running products calculated by the second backward loop are
# accumelated products based on the running products calculated by the first
# loop.
#
# By this setup, each elements in the result array would be the running product
# of all the values to its left and right.
#
# Complexity:
# O(n) time | O(n) space - where n is the length of the input array.
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]

  leftRunningProduct = 1
  for i in range(len(array)):
    products[i] = leftRunningProduct
    leftRunningProduct *= array[i]

  rightRunningProduct = 1
  for i in reversed(range(len(array))):
    products[i] = rightRunningProduct
    rightRunningProduct *= array[i]

  return products
