#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure nums1 is the smaller array to optimize binary search
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1);
        
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        int half = (total + 1) / 2;
        
        int left = 0, right = m;
        
        while (left <= right) {
            int i = left + (right - left) / 2;  // partition index for nums1
            int j = half - i;                    // partition index for nums2
            
            int nums1_left = (i == 0) ? INT_MIN : nums1[i - 1];
            int nums1_right = (i == m) ? INT_MAX : nums1[i];
            
            int nums2_left = (j == 0) ? INT_MIN : nums2[j - 1];
            int nums2_right = (j == n) ? INT_MAX : nums2[j];
            
            if (nums1_left <= nums2_right && nums2_left <= nums1_right) {
                // Correct partition found
                if (total % 2 == 1) {
                    return double(max(nums1_left, nums2_left));
                } else {
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0;
                }
            } else if (nums1_left > nums2_right) {
                right = i - 1;
            } else {
                left = i + 1;
            }
        }
        
        // If input arrays are valid, this line will never be reached
        return 0.0;
    }
};
