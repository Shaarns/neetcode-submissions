class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #[1, 2, 5, 6, 50] #[10, 20, 30]
        #[1, 2, 5, 6, 10, 20,  30, 50]
        #[1, 2] #[3]
        #[1, 2, 3]
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        half = total_len//2 # 3//2 = 1

        l = 0
        r = len(nums2)#1-1 = 0

        while l<=r:
            m = (l+r)//2 #0//2 = 0

            nums1_half = half - m # 1-0=1
            nums1_left = nums1[nums1_half - 1] if nums1_half > 0 else float('-inf') #1-1=0=1
            nums1_right = nums1[nums1_half] if nums1_half < len(nums1) else float('inf')#2
            nums2_left = nums2[m-1] if m > 0 else float('-inf') #-inf
            nums2_right = nums2[m] if m < len(nums2) else float('inf') #3

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # found the correct halfs so now we can return
                if total_len % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)

            if nums1_left > nums2_right:
                l = m + 1
            elif nums2_left > nums1_right:
                r = m - 1

            

