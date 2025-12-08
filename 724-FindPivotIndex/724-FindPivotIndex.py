# Last updated: 12/8/2025, 8:54:28 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        if len(nums)<1:
4            return -1
5        total_sum = sum(nums)
6
7        left_sum = 0
8        for i in range(0,len(nums)):
9            if left_sum==(total_sum - left_sum - nums[i]):
10                return i
11            left_sum+=nums[i]
12        
13        return -1