class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, num in enumerate(nums):
            sol = target - num
            if sol in map:
                print map
                return [map[sol], idx] 
            map[num] = idx
        return [-1, -1]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
