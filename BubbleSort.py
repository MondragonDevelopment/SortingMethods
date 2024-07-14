# O(n^2) Time | O(1) Space

def bubbleSort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        counter += 1                                            # Each time we traverse the array, the largest number gets in place, so we limit the range of sorting
    return array

nums = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(nums))        
