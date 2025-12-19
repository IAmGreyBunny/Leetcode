# Last updated: 12/19/2025, 11:15:16 AM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        count = {}
4
5        for num in arr:
6            if num in count:
7                count[num] += 1
8            else:
9                count[num] =1
10        
11        if len(set(count.values())) == len(count):
12            return True
13        else:
14            return False