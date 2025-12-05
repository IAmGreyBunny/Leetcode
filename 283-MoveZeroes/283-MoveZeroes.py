# Last updated: 12/5/2025, 5:25:46 PM
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
15                if i<j:
16                    j=i
17                i+=1
18            else:
19                nums[i],nums[j] = nums[j],nums[i]
20                while j<=i:
21                    if nums[j]==0:
22                        break
23                    else:
24                        j+=1
25                i+=1
26
27        
28
29        
30
31