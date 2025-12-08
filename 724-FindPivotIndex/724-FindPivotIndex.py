# Last updated: 12/8/2025, 8:52:31 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total_sum = sum(nums)
4        print(total_sum)
5
6        left_sum = 0
7        for i in range(0,len(nums)):
8            right_sum = total_sum - left_sum - nums[i]
9            if left_sum==right_sum:
10                return i
11            left_sum+=nums[i]
12        
13        return -1