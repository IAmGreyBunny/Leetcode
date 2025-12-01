# Last updated: 12/1/2025, 4:09:26 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        result = [False for _ in candies]
4        currentMax = max(candies)
5
6        i = 0 
7        while(i<len(candies)):
8            if candies[i] + extraCandies >= currentMax:
9                result[i] = True
10            else:
11                result[i] = False
12            i+=1
13        
14        return result
15