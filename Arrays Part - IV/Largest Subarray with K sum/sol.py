class Solution:
    def longestSubarray(self, nums, k):
        max_len = 0
        n = len(nums)

        for i in range(n):
            curr_sum = 0

            for j in range(i, n):
                curr_sum += nums[j]

                if curr_sum == k:
                    max_len = max(max_len, j - i + 1)

        return max_len