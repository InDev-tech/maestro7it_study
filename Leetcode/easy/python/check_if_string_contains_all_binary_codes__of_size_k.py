class Solution(object):
    def hasAllCodes(self, s, k):
        need = 1 << k
        if len(s) < need + k - 1:
            return False
        possibls = set()
        n = 2**k
        for i in range(len(s)-k+1):
            possibls.add(s[i:i+k])
        if len(possibls) == n:
            return True
        return False

result = Solution()
print(result.hasAllCodes('00110110', 2))