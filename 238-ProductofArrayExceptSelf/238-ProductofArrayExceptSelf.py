# Last updated: 12/12/2025, 12:01:10 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if len(nums) < 1:
4            return []
5        
6        product = 1
7        zero_counter = 0
8        for num in nums:
9            if num == 0:
10                zero_counter+=1
11            else:
12                product*=num
13            if zero_counter==2:
14                return [0 for x in range(0,len(nums))]
15
16        answer=[]
17
18        if zero_counter==1:
19            for i in range(0,len(nums)):
20                if nums[i] != 0:
21                    answer.append(0)
22                else:
23                    answer.append(product)
24            return answer
25
26        
27        for i in range(0,len(nums)):
28            if nums[i]==0:
29                answer.append(product)
30            else:
31                answer.append(product//nums[i])
32        return answer
33