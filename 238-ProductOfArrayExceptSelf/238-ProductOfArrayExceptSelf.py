# Last updated: 11/30/2025, 5:39:56 PM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        #Get prefixes
        for i in range(0,len(nums)):
            if i==0:
                prefix[i] = 1
            elif i==1:
                prefix[i] = nums[0]
            else:
                prefix[i] = prefix[i-1] * nums[i-1]

        print("Prefix: ")
        print(prefix)
    
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postfix[i] = 1
            elif i == len(nums)-2:
                postfix[i] =nums[len(nums)-1]
            else:
                postfix[i] = postfix[i+1] * nums[i+1]

        print("Postfix:")
        print(postfix)

        result = [1] * len(nums)
        for i in range(0,len(nums)):
            result[i] = prefix[i] * postfix[i]

        return result
        
        
        