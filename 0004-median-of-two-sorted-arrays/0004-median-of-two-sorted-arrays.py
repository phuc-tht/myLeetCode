class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge = []

        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                merge.append(nums1.pop(0))
            else:
                merge.append(nums2.pop(0))

        if nums1:
            merge += nums1
        if nums2:
            merge += nums2  
            
        if len(merge) % 2 == 1:
            return(merge[len(merge) // 2])
        else:
            return((merge[len(merge) // 2] + merge[len(merge) // 2 - 1]) / 2)