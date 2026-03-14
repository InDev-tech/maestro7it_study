# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         nums1 = nums1[:m]
#         nums1 = nums1 + nums2
#         nums1.sort()
#         return nums1

# result = Solution()
# print(result.merge([1,2,3,0,0,0], 3, [2,5,6], 3))



class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Сливает nums2 в nums1 in-place.
        nums1 имеет размер m + n, первые m элементов — значимые.
        Метод изменяет nums1 напрямую и ничего не возвращает.
        """
        write = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1