# Last updated: 10/12/2026, 4:45:54 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy=candies[0]
        result = []
        
        for i in range(0,len(candies)):
            if candies[i] >= max_candy:
                max_candy = candies[i] 

        for i in range(0,len(candies)):
            if (candies[i] + extraCandies) >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result
