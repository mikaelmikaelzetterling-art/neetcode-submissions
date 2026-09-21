class Solution:
    def maxArea(self, heights: List[int]) -> int:
        values = []

        left = 0
        right = 1 

        for i in range(len(heights)-1):
            area = min(heights[left], heights[len(heights)-right]) * (len(heights)-right  - left)
            values.append(area)
            if heights[left] <= heights[len(heights)-right]:
                left += 1
            elif heights[left] > heights[len(heights)-right]:
                right += 1
        return max(values)
        