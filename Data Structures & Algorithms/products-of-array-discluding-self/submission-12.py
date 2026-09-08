class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]

        n = len(nums)
        res = [1] * n
        prefix = []
        suffix = [0] * n

        left_product = 1
        for num in nums:
            prefix.append(left_product)
            left_product *= num

        right_product = 1
        for i in range(n-1, -1, -1):
            res[i] = right_product * prefix[i]
            right_product *= nums[i]


        return res