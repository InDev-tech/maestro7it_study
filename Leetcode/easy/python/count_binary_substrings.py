class Solution(object):
    def countBinarySubstrings(self, s):
        ans = 0
        groups = []
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                groups.append(len(s[:i+1]))
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1])
        return ans

result = Solution()
print(result.countBinarySubstrings('00110011'))