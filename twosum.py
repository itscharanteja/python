from typing import List


class twosums:
    def sum(self, num: List[int], target: int):
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[j] == target - num[i]:
                    return (i, j)


a = twosums()

my = [4,3,2,1]

print(a.sum(my, 3))
