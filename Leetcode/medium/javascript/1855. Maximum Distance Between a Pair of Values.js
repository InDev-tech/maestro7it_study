/**
 * Находит максимальное расстояние между валидной парой индексов (i, j),
 * где i <= j и nums1[i] <= nums2[j].
 * 
 * @param {number[]} nums1 - первый невозрастающий массив
 * @param {number[]} nums2 - второй невозрастающий массив
 * @return {number} максимальное расстояние (j - i) или 0
 */
var maxDistance = function(nums1, nums2) {
    let i = 0, j = 0, maxDist = 0;
    
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] <= nums2[j]) {
            if (i <= j) {
                maxDist = Math.max(maxDist, j - i);
            }
            j++;
        } else {
            i++;
        }
    }
    return maxDist;
};