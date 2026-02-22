class Solution(object):
    def binaryGap(self, n):
        n = bin(n)[2:]
        max_dist = 0
        last_one = -1
        for i, bit in enumerate(n):
            if bit == '1':
                if last_one != -1:
                    if max_dist < (i - last_one):
                        max_dist = i - last_one
                last_one = i
        return max_dist

result = Solution()
print(result.binaryGap(5))