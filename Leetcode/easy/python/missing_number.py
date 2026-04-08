class Solution(object):
    def missingNumber(self, nums):
        total_sum = 0
        for i in range(1, len(nums) + 1):
            total_sum += i
        return total_sum - sum(nums)