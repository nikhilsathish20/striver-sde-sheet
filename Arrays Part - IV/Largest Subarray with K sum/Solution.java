class Solution {
    public int longestSubarray(int[] nums, int k) {
        int left = 0, right = 0;
        long sum = 0;
        int maxLen = 0;

        while (right < nums.length) {
            sum += nums[right];

            while (left <= right && sum > k) {
                sum -= nums[left];
                left++;
            }

            if (sum == k) {
                maxLen = Math.max(maxLen, right - left + 1);
            }

            right++;
        }

        return maxLen;
    }
} {
    
}
