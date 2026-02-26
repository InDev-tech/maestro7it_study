class Solution(object):
    def sortByBits(self, arr):
        lst = []
        for i in range(len(arr)):
            arr[i] = (bin(arr[i]).count('1'), arr[i])
        arr.sort()
        for el in arr:
            lst.append(el[1])
        return lst
    
result = Solution()
print(result.sortByBits([0,1,2,3,4,5,6,7,8]))