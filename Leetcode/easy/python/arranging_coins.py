class Solution(object):
    def arrangeCoins(self, n):
        if n == 1:
            return 1
        left, right = 1, n
        k = 0
        while left <= right:
            mid = left + (right - left) // 2
            if (mid + 1) * mid <= 2 * n:
                k = mid
                left = mid + 1
            else:
                right = mid - 1
        return k

if __name__ == '__main__':
    result = Solution()
    print(result.arrangeCoins(8))