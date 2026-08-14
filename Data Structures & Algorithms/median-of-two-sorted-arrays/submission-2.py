class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #[1, 4, 5, 6, 7, 8] #[2, 3, 9, 10]
        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        l = 0
        r = 0
        new_arr = []

        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                new_arr.append(nums1[l])
                l += 1
            else:
                new_arr.append(nums2[r])
                r += 1

        while l < len(nums1):
            new_arr.append(nums1[l])
            l += 1
        while r < len(nums2):
            new_arr.append(nums2[r])
            r += 1


        mid = len(new_arr) // 2
        if len(new_arr) % 2 == 0:
            return (new_arr[mid] + new_arr[mid-1]) / 2
        else:
            return new_arr[mid]