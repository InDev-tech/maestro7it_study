class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

result = Solution()
print(result.intersection([1,2,2,1], [2,2]))