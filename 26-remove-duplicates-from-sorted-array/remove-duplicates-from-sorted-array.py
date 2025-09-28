class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # pointer for the place of the next unique element
        k = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # found a unique element
                nums[k] = nums[i]       # move it to the front
                k += 1
        
        return k
