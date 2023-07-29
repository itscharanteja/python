import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self,nums:List[int],k:int)->List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]  
    
    
c= Solution()

ly = [1,1,1,2,3,3,3,3,4,2,2]
print(c.topKFrequent(ly,2))