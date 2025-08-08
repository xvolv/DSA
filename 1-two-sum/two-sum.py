class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store number and its index
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
        
        # According to the problem, there is always exactly one solution,
        # so no need for a return here
