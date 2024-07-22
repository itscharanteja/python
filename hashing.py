def containsDuplicate(nums):
    occur = {}
    for num in nums:
        if num in occur:
            occur[num] += 1
        else:
            occur[num] = 1
    for key,value in occur.items():
        if value>1:
            return True
print(containsDuplicate([1,2,3,1]))