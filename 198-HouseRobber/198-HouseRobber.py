# Last updated: 12/9/2025, 12:22:18 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        max_profit = [0 for x in range(0,len(nums))]
4
5        # Edge cases and initial declaration
6        if len(nums) == 0:
7            return 0
8        elif len(nums) == 1:
9            return nums[0]
10        elif len(nums) == 2:
11            return nums[0] if nums[0] > nums[1] else nums[1]
12        else:
13            max_profit[0] = nums[0]
14            max_profit[1] = nums[0] if nums[0] > nums[1] else nums[1]
15        
16        for i in range(1,len(nums)):
17            if max_profit[i-2] + nums[i] > max_profit[i-1]:
18                max_profit[i] = max_profit[i-2]+nums[i]
19            else:
20                max_profit[i] = max_profit[i-1]
21
22        current_max = max_profit[len(nums)-1]
23        for i in range(len(max_profit)-1,len(max_profit)-3,-1):
24            if max_profit[i] > current_max:
25                current_max = max_profit[i]
26
27        return current_max
28