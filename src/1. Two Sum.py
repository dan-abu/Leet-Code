# Question can be found using this link: https://leetcode.com/problems/two-sum/
# Solution below

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tries = len(nums) - 1
        count = 0
        while count < tries:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    guess = nums[i] + nums[j]
                    if guess == target:
                        return [i, j]
                    else:
                        continue
                count += 1

"""Example inputs"""
# nums1 = [3,2,4]
# target1 = 6

# nums1 = [2,7,11,15]
# target1 = 9

# nums1 = [3,3]
# target1 = 6

nums1 = [3,2,3]
target1 = 6

t = Solution()
t.twoSum(nums1, target1)