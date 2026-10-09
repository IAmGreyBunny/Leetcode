# Last updated: 10/9/2026, 11:08:59 PM
1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3        if k==len(nums):
4            return sum(nums[0:k])/k
5
6        nums=[float(nums[i])/k for i in range(0,len(nums))]
7
8        win_avg = sum(nums[0:k])
9        current_max = win_avg
10
11
12        i = 1
13        while i<len(nums) and (i+(k-1))<len(nums):
14            win_avg = win_avg - nums[i-1] + nums[i+(k-1)]
15            if win_avg>current_max:
16                current_max = win_avg
17            i+=1
18            
19
20        return current_max