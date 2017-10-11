class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: 
                    max_of_left = B[j-1]
                elif j == 0: 
                    max_of_left = A[i-1]
                else: 
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: 
                    min_of_right = B[j]
                elif j == n: 
                    min_of_right = A[i]
                else: 
                    min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0
        


    def findMedianHelper(self, nums, i, j):
        length = j - i
        if length % 2 == 1:
            return [nums[(i + j)/2], (length - 1) / 2]
        else:
            return [(nums[(i + j)/2] + nums[(i + j + 2)/2]) / 2.0, (length - 1) / 2]
    
    def stupid(self, nums1, nums2):
        nums1.extend(nums2)
        num = sorted(nums1)
        length = len(num)
        return num[(length - 1)/2] if length % 2 == 1 \
            else (num[(length - 1)/2] + num[length/2]) / 2.0


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    # print(s.findMedianSortedArrays(nums1, nums2))
    print(s.stupid(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    # print(s.findMedianSortedArrays(nums1, nums2))
    print(s.stupid(nums1, nums2))