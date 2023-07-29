from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums.sort()
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return nums[:l], len(nums[:l])


n = [0, 1, 2, 1, 2, 3, 1]
print(removeDuplicates(n))
