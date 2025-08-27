class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Mapping digits to letters
        digit_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        result = []
        
        # Backtracking helper function
        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            letters = digit_to_char[digits[index]]
            for letter in letters:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(sol.letterCombinations(""))    # []
print(sol.letterCombinations("2"))   # ["a","b","c"]
