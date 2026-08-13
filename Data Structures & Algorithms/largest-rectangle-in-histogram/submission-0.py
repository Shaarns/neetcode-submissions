class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = float('-inf')

        for i, curr_height in enumerate(heights):
            min_i = i

            while stack and stack[-1][0] >= curr_height:
                prev_height, prev_i = stack.pop()
                min_i = prev_i
                area = (i - prev_i) * prev_height
                max_area = max(max_area, area)

            stack.append((curr_height, min_i))

        for height, indx in stack:
            area = (len(heights) - indx) * height
            max_area = max(max_area, area)

        return max_area
