class Solution(object):
    def isPerfectSquare(self, num):
        if num == 0 or num == 1:
            return True
        left = 1
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False