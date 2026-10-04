# Last updated: 10/4/2026, 4:36:42 PM
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        """
4        :type flowerbed: List[int]
5        :type n: int
6        :rtype: bool
7        """
8        if n==0:
9            return True
10
11        for i in range(0,len(flowerbed)):
12            if flowerbed[i] == 0:
13                if flowerbed[max(0,i-1)]==0 and flowerbed[min(len(flowerbed)-1,i+1)]==0:
14                    flowerbed[i]=1
15                    n-=1
16                    if n==0:
17                        return True
18            else:
19                continue
20        
21        return False