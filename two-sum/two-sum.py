class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()
        for i,n in enumerate(nums):
            if n in seen:
                return [i, seen[n]]
            seen[target-n] = i
            