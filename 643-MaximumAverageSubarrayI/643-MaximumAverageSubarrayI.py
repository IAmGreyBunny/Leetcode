# Last updated: 10/9/2026, 11:14:29 PM
1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3        if k==len(nums):
4            return sum(nums[0:k])/k
5
6        current_sum = sum(nums[:k])
7        current_max = current_sum
8        
9        i = 1
10        while i<len(nums) and (i+(k-1))<len(nums):
11            current_sum = current_sum - nums[i-1] + nums[i+(k-1)]
12            if current_sum>current_max:
13                current_max = current_sum
14            i+=1
15            
16
17        return current_max/k