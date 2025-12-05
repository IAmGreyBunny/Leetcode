# Last updated: 12/5/2025, 5:45:31 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        i = 0 
7        j = 0 #points to the first 0 from the left
8
9        if len(nums)<=1:
10            return nums
11        
12
13        while i<len(nums) and j<len(nums):
14            if nums[i]==0:
15                i+=1
16            else:
17                if i >= j:
18                    nums[i],nums[j] = nums[j],nums[i]
19                i+=1
20
21            # Find next zero
22            while j<len(nums):
23                if nums[j]==0:
24                    break
25                if j==len(nums)-1:
26                    return nums
27                j+=1
28
29        
30
31        
32
33