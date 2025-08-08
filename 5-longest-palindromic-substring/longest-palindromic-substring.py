class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            max_len = max(len1, len2)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]


# Test
sol = Solution()
print(sol.longestPalindrome("babad"))  # bab or aba
print(sol.longestPalindrome("cbbd"))   # bb
