# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        unique_elements = []

        for num in nums:
            if num not in unique_elements:
                unique_elements.append(num)

        nums[:] = unique_elements

        return len(unique_elements)
