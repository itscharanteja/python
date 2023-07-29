class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[-1]:
            return True
        else:
            return False


x = Solution()

print(x.isPalindrome(121))
        
