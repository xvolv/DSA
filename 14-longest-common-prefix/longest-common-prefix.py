class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the prefix being the first string
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Shorten the prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""  # No common prefix
        
        return prefix
