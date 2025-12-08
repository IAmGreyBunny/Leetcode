# Last updated: 12/8/2025, 6:47:02 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        if len(nums) < 1:
4            return -1
5
6        left_sum = [nums[0]]
7        right_sum = [nums[len(nums)-1]]
8
9        for i in range(1,len(nums)):
10            left_sum.append(left_sum[-1] + nums[i])
11            right_sum.append(right_sum[-1] + nums[len(nums)-1-i])
12        
13        right_sum.reverse()
14
15        print(f"L:{left_sum}\nR:{right_sum}")
16
17        for i in range(0,len(nums)):
18            if i==0 and left_sum[0]==right_sum[0]:
19                return 0 
20            elif i == len(nums)-1 and left_sum[len(nums)-1] == right_sum[len(nums)-1]:
21                return len(nums)-1
22            elif i+2 < len(nums) and left_sum[i]==right_sum[i+2]:
23                return i+1
24        
25        return -1