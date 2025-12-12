# Last updated: 12/12/2025, 10:22:22 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if len(nums) < 1:
4            return []
5        if len(nums) == 1:
6            return [0]
7
8        prefix = [1]
9        postfix = [1]
10
11        for i in range(1,len(nums)):
12            prefix.append(prefix[i-1]*nums[i-1])
13            postfix.append(postfix[i-1]*nums[len(nums)-i])
14
15        answers = []
16        for i in range(0,len(prefix)):
17            answers.append(prefix[i] * postfix[len(postfix)-1-i])
18
19        return answers
20
21
22
23