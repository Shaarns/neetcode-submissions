class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = [0] * len(height)

        left_max = 0
        right_max = 0
        for num in height:
            prefix.append(left_max)
            left_max = max(left_max, num)

        for i in range(len(height) - 1, -1, -1):
            suffix[i] = right_max
            right_max = max(right_max, height[i])
        
        water_trapped = 0
        for i in range(len(height)):
            water_trapped  += max(min(prefix[i], suffix[i]) - height[i], 0)

        return water_trapped
