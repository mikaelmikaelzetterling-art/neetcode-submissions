
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        antal_nollor = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                antal_nollor += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                antal_nollor += right_max - height[right]
                right -= 1

        return antal_nollor
