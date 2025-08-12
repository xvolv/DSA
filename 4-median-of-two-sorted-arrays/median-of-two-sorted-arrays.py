class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2  # +1 ensures correct handling for odd lengths

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition in nums1
            j = half_len - i         # Partition in nums2

            # Get the elements just before and after the partition
            max_left1 = float('-inf') if i == 0 else nums1[i-1]
            min_right1 = float('inf') if i == m else nums1[i]

            max_left2 = float('-inf') if j == 0 else nums2[j-1]
            min_right2 = float('inf') if j == n else nums2[j]

            # Check if we have a valid partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if total_len % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return float(max(max_left1, max_left2))
            elif max_left1 > min_right2:
                right = i - 1  # Too far right in nums1, move left
            else:
                left = i + 1   # Too far left in nums1, move right
