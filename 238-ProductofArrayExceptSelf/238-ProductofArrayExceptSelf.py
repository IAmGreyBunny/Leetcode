# Last updated: 12/12/2025, 10:22:37 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if len(nums) < 1:
4            return []
5
6        prefix = [1]
7        postfix = [1]
8
9        for i in range(1,len(nums)):
10            prefix.append(prefix[i-1]*nums[i-1])
11            postfix.append(postfix[i-1]*nums[len(nums)-i])
12
13        answers = []
14        for i in range(0,len(prefix)):
15            answers.append(prefix[i] * postfix[len(postfix)-1-i])
16
17        return answers
18
19
20
21