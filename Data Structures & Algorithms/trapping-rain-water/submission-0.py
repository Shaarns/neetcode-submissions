class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            l, r = i-1, i+1
            maxLeft = 0
            while l >= 0:
                if maxLeft < height[l]:
                    maxLeft = height[l]
                l -= 1
            maxRight = 0
            
            while r < len(height):
                if maxRight < height[r]:
                    maxRight = height[r]
                r += 1

            waterTrap = min(maxLeft, maxRight) - height[i]
            if waterTrap > 0:
                max_water += waterTrap 
            
        return max_water