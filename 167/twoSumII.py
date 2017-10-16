class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        diction = {}
        for (idx, num) in enumerate(numbers):
            search = target - num
            if search in diction:
                return diction[search] + 1, idx + 1
            diction[num] = idx
        return [0, 0]

if __name__ == '__main__':
    numbers = (2, 7, 11, 15)
    target = 9
    idx1, idx2 = Solution().twoSum(numbers, target)
    print idx1, idx2