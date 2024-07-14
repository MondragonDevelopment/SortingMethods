# O(n^2) Time | O(1) Space

def insSortRec(seq, i):
    if i == 0: return
    insSortRec(seq, i-1)
    print(seq)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def insSort(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq
        
nums = [8, 5, 2, 9, 5, 6, 3]
length = len(nums) - 1
# print(insSort(nums))
print(insSortRec(nums, length))
