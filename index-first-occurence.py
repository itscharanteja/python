class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack = haystack.lower()
        needle = needle.lower()
        if needle == "":
            return 0
        for l in range(len(haystack)+1 - len(needle)):

            if haystack[l:l + len(needle)] == needle:
                return l
        return -1
        # or for one line solution👇
        # return haystack.find(needle)


i = Solution()
print(i.strStr("Sadbutnotsad", "sad"))
