class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        start1 = 0
        end1 = len(nums1) - 1
        start2 = 0
        end2 = len(nums2) - 1
        