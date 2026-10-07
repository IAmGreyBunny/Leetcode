# Last updated: 10/8/2026, 12:41:11 AM
1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        for i in range(0,len(nums)):
7            if nums[i] != 0:
8                continue
9            else:
10                for j in range(min(len(nums),i+1),len(nums)):
11                    if nums[j]!=0:
12                        nums[i],nums[j] = nums[j],nums[i]
13                        break
14            
15        