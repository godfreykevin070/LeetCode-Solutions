class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        while (nums[i] + nums[j]) != target:
            if j == (len(nums)-1):
                i = i + 1
                j = i + 1
            else:
                j = j + 1
        return [i,j]

        