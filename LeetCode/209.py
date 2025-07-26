from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_of_subarray = 0
        min_length = int(1e9)
        for right in range(len(nums)):
            sum_of_subarray += nums[right]
            
            while sum_of_subarray >= target:
                min_length = min(min_length, right - left + 1)
                sum_of_subarray -= nums[left]
                left += 1
        if min_length != int(1e9):
            return min_length
        else:
            return 0

test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))