# Last updated: 12/12/2025, 12:02:09 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if len(nums) < 1:
4            return []
5        
6        product = 1
7        zero_counter = 0
8        
9        for num in nums:
10            if num == 0:
11                zero_counter+=1
12            else:
13                product*=num
14            if zero_counter==2:
15                return [0 for x in range(0,len(nums))]
16
17        answer=[]
18
19        if zero_counter==1:
20            for i in range(0,len(nums)):
21                if nums[i] != 0:
22                    answer.append(0)
23                else:
24                    answer.append(product)
25            return answer
26        else:
27            for i in range(0,len(nums)):
28                if nums[i]==0:
29                    answer.append(product)
30                else:
31                    answer.append(product//nums[i])
32            return answer
33