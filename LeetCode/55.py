from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        for i in range(len(nums)):
            if i > maxIdx:
                return False
            maxIdx = max(maxIdx, i + nums[i])
            if maxIdx >= len(nums) -1:
                return True
        return False


test = Solution()
print(test.canJump([2,3,1,1,4]))
print(test.canJump([3,2,1,0,4]))