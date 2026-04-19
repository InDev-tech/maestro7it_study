class Solution {
public:
    /**
     * Находит максимальное расстояние между валидной парой индексов (i, j),
     * где i <= j и nums1[i] <= nums2[j].
     * 
     * @param nums1 первый невозрастающий массив
     * @param nums2 второй невозрастающий массив
     * @return максимальное расстояние (j - i) или 0
     */
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0, max_dist = 0;
        int len1 = nums1.size(), len2 = nums2.size();
        
        while (i < len1 && j < len2) {
            if (nums1[i] <= nums2[j]) {
                if (i <= j) {
                    max_dist = max(max_dist, j - i);
                }
                j++;
            } else {
                i++;
            }
        }
        return max_dist;
    }
};