#O(n^2)
def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(0,n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]

array = [9,8,7,6,5,4,3,2,1,0]
bubblesort(array)
print(array)