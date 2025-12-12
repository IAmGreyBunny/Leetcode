# Last updated: 12/12/2025, 11:41:01 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if len(nums) < 1:
4            return []
5
6        prefix = 1
7        postfix = 1
8        answers = [prefix]
9        n = len(nums)
10
11        for i in range(0,n-1):
12            prefix*=nums[i]
13            answers.append(prefix)
14
15        for i in range(n-1,-1,-1):
16            answers[i]*=postfix
17            postfix *= nums[i]
18
19        return answers
20
21
22
23