class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        mid = len(nums1)//2
        if len(nums1)%2 != 0:
            return float(nums1[mid])
        else:
            return (nums1[mid]+nums1[mid-1])/2