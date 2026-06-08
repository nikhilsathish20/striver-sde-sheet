class Solution:
    def subarraysWithXorK(self, nums, k):
        xor_map = {0: 1}

        xr = 0
        count = 0

        for num in nums:
            xr ^= num

            x = xr ^ k

            count += xor_map.get(x, 0)

            xor_map[xr] = xor_map.get(xr, 0) + 1

        return count