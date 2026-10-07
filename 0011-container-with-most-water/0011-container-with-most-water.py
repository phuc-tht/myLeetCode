class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_water = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]: left += 1
            else: right -= 1
            max_water = max(max_water, (right - left) * min(height[left], height[right]))    
        return(max_water)