class Solution:
    def maxDistance(self, nums1, nums2):
        """
        Находит максимальное расстояние между валидной парой индексов (i, j),
        где i <= j и nums1[i] <= nums2[j].
        
        Параметры:
        nums1: List[int] - первый невозрастающий массив
        nums2: List[int] - второй невозрастающий массив
        
        Возвращает:
        int - максимальное расстояние (j - i) или 0, если валидных пар нет
        """
        i = j = max_dist = 0
        len1, len2 = len(nums1), len(nums2)
        
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                if i <= j:
                    max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
        return max_dist