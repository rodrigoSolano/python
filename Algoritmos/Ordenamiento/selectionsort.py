def selectionSort(array):
  n = len(array)
  for i in range(n):
    # Initially, assume the first element of the unsorted part as the minimum.
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):
        # Update position of minimum element if a smaller element is found.
        minimum = j

    # Swap the minimum element with the first element of the unsorted part.     
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    
  return array

# Driver code
array = [13, 4, 9,0, 5, 3, 16, 12]
print(selectionSort(array))
