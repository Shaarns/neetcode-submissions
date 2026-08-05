class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            minHeight = min(heights[l], heights[r])

            area = width * minHeight
            maxArea = max(area, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea