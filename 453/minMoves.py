class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        sum_val = sum(nums)
        print min_val, sum_val        
        return sum_val - len(nums) * min_val

if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3]
    print s.minMoves(A)
