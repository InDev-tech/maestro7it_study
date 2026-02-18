class Solution(object):
    def hasAlternatingBits(self, n):
        n = bin(n)[2:]
        for i in range(len(n)-1):
            if n[i] == n[i+1]:
                return False
        else:
            return True