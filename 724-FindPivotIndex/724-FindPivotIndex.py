# Last updated: 12/8/2025, 8:54:47 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        if len(nums)<1:
4            return -1
5            
6        total_sum = sum(nums)
7
8        left_sum = 0
9        for i in range(0,len(nums)):
10            if left_sum==(total_sum - left_sum - nums[i]):
11                return i
12            left_sum+=nums[i]
13        
14        return -1