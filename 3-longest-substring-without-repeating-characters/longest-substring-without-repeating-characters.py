class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If duplicate found, shrink window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to the set
            char_set.add(s[right])
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length
