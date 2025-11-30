# Last updated: 11/30/2025, 5:39:55 PM
class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0

        while i < len(nums):
            if nums[i]==0:
                j=i+1
                while j<len(nums):
                    if nums[j] !=0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
                    j+=1
            
            i+=1
        