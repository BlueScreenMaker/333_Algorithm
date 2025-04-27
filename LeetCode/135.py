from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                result[j] = max(result[j], result[j+1] + 1)

        return sum(result)
    
test = Solution()
print(test.candy([1,0,2]))