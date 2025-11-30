# Last updated: 11/30/2025, 5:39:53 PM
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False

        i = float('inf')
        j = float('inf')

        for num in nums:
            if num > j:
                return True
            else:
                if num <= i:
                    i = num
                elif num < j:
                    j = num

        return False
        