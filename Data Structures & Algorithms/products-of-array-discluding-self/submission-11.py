class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 1, 2, 8]
        #[48, 24, 6, 1]

        n = len(nums)
        prefix = []
        suffix = [0] * n

        left_product = 1
        for num in nums:
            prefix.append(left_product)
            left_product *= num

        right_product = 1
        for i in range(n-1, -1, -1):
            suffix[i] = right_product
            right_product *= nums[i]


        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res