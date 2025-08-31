class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:  # closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:  # opening bracket
                stack.append(char)

        return not stack
