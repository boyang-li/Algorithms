# O(n) time | O(1) space - n is the length of the array
def moveElementToEnd(array, toMove):
  i, j = 0, len(array) - 1

  while i < j:
    # this check for i < j is very important!
    while i < j and array[j] == toMove:
        j -= 1    
    if array[i] == toMove:
      array[i], array[j] = array[j], array[i]
    i += 1

  return array