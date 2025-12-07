# Last updated: 12/7/2025, 8:47:00 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        max_height = 0 
4        current = 0
5
6        for i in range(0,len(gain)):
7            current += gain[i]
8            if current >= max_height:
9                max_height = current
10            
11        return  max_height