class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            # Edge values handling boundary conditions
            a_left = nums1[i - 1] if i > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_left = nums2[j - 1] if j > 0 else float('-inf')
            b_right = nums2[j] if j < n else float('inf')

            # Check if partition is valid
            if a_left <= b_right and b_left <= a_right:
                # Odd total length
                if (m + n) % 2 != 0:
                    return float(max(a_left, b_left))
                # Even total length
                return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
            
            elif a_left > b_right:
                high = i - 1  # Too far right in nums1
            else:
                low = i + 1   # Too far left in nums1

        return 0.0
        