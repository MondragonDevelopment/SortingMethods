# O(n^2) Time | O(1) Space

def selSort(array):
    counter = 0
    while counter < len(array) - 1:
        smallest = counter
        for i in range(counter + 1, len(array)):
            if array[smallest] > array[i]:
                smallest = i
        array[counter], array[smallest] = array[smallest], array[counter]
        counter += 1
    return array

def selSort2(array):
    for i in range(len(array) - 1, 0, -1):
        greatest = i
        for j in range(i):
            if array[j] > array[greatest]:
                greatest = j
        array[i], array[greatest] = array[greatest], array[i]
    return array

def selSortRec(array, lastIdx):
    if lastIdx == 0: return
    greatest = lastIdx
    for j in range(lastIdx):
        if array[j] > array[greatest]:
            greatest = j
        array[lastIdx], array[greatest] = array[greatest], array[lastIdx]
    selSortRec(array, lastIdx - 1)
    return array



nums = [8, 5, 2, 9, 5, 6, 3]
print(selSort2(nums))
print(selSortRec(nums, lastIdx = len(nums) - 1))