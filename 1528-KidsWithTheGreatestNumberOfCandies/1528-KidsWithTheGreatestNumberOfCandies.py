# Last updated: 11/30/2025, 5:39:45 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = candies[0]
        result = []

        for i in range(0,len(candies)):
            if candies[i] > max_candies:
                max_candies = candies[i]
        
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result