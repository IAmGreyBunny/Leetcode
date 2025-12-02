# Last updated: 12/2/2025, 3:48:14 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        remaining_flower = n
4
5        # no need check
6        if remaining_flower == 0:
7            return True
8
9        print(remaining_flower)
10        
11        # if only one element
12        if len(flowerbed)==1 and flowerbed[0]==0:
13            if remaining_flower-1==0:
14                return True
15            else:
16                return False
17        
18        # if more than one element
19        i = 0
20        while(i<len(flowerbed)):
21            if flowerbed[i]==0:
22                if i == 0:
23                    if flowerbed[i+1]==0:
24                        remaining_flower-=1
25                        flowerbed[i]=1
26                elif i == len(flowerbed)-1:
27                    if flowerbed[i-1]==0:
28                        remaining_flower-=1
29                        flowerbed[i]=1
30                elif flowerbed[i+1]==0 and flowerbed[i-1]==0:
31                    remaining_flower-=1
32                    flowerbed[i]=1
33    
34            i+=1
35            if remaining_flower == 0:
36                return True
37
38        return False