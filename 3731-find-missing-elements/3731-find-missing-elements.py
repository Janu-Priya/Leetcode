class Solution(object):
    def findMissingElements(self, nums):
        """:type nums: List[int]

     :rtype: List[int]
    """
        num_set = set(nums)
        min_val, max_val = min(nums), max(nums)

        return [x for x in range(min_val, max_val + 1) if x not in num_set]
        