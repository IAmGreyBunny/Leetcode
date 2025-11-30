# Last updated: 11/30/2025, 5:40:01 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        current_index=0
        
        while(current_index!=len(nums)):
            for i in range(current_index+1,len(nums)):
                if nums[current_index] + nums[i] == target:
                    return [current_index,i]
            current_index+=1
        