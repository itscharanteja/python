import math


def bin_search(sorted, target):
    index = math.ceil(len(sorted)/2)
    while target != sorted[index]:
        if sorted[index] > target:
            index = math.ceil(index/2)
        else:
            index = math.ceil(index+index/2)
    return index


my_Arr = []

print(bin_search(my_Arr,3))