class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Step 1: Sort the array
        closest_sum = float('inf')  # Initialize with infinity

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum if the current one is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers
                if current_sum < target:
                    left += 1  # Need a bigger sum
                elif current_sum > target:
                    right -= 1  # Need a smaller sum
                else:
                    return current_sum  # Perfect match

        return closest_sum
