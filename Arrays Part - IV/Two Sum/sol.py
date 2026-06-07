class Solution:
    def twoSum(self, nums, target):
        memo = {}

        for j in range(0, len(nums)):
            num = nums[j]
            complement = target-num
            if (complement in memo.keys()):
                i = memo[complement]
                return [i, j]

            memo[num] = j

        return -1