from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_volume = 0
        while left < right:
            width = right - left
            min_height = min(height[right], height[left])
            max_volume = max(max_volume, min_height * width)
        
            # 왼쪽이 높은 경우
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_volume