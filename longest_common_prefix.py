from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = sorted(strs)
        base = str[0]

        for i in range(len(base)):
            for word in str[1:]:
                if(base[i] != word[i] or i == len(word)):
                    return base[0:i]
        return base


a = Solution()

mylist = ["flow","flower","flight"]

print(a.longestCommonPrefix(mylist))