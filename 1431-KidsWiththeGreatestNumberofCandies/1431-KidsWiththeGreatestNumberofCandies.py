# Last updated: 10/2/2026, 11:28:32 PM
1class Solution(object):
2    def kidsWithCandies(self, candies, extraCandies):
3        """
4        :type candies: List[int]
5        :type extraCandies: int
6        :rtype: List[bool]
7        """
8        max_candy=candies[0]
9        result = []
10        
11        for i in range(0,len(candies)):
12            if candies[i] >= max_candy:
13                max_candy = candies[i]
14                
15
16        for i in range(0,len(candies)):
17            if (candies[i] + extraCandies) >= max_candy:
18                result.append(True)
19            else:
20                result.append(False)
21
22        return result
23