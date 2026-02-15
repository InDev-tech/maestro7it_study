class Solution(object):
    def addBinary(self, a, b):
        a_int = 0
        b_int = 0
        for i in range(len(a)):
            a_int += int(a[-i-1])* 2**i
        for i in range(len(b)):
            b_int += int(b[-i-1])* 2**i
        return bin(a_int + b_int)[2:]
            

result = Solution()
print(result.addBinary('1010', '1011'))