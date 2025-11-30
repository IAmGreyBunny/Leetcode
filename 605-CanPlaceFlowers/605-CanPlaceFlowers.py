# Last updated: 11/30/2025, 5:39:49 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = n

        for i in range(0,len(flowerbed)):
            if flowers == 0:
                break

            if flowerbed[i] == 1:
                continue
            
            if i-1 >= 0 and i+1 < len(flowerbed):
                if flowerbed[i-1] != 1 and flowerbed[i+1] !=1:
                    flowerbed[i] = 1
                    flowers -= 1
            elif i-1 >= 0 and i+1 >= len(flowerbed):
                if flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    flowers -= 1
            elif i-1 < 0 and i+1 < len(flowerbed):
                if flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    flowers -= 1
            else:
                flowerbed[i] =1
                flowers -= 1

                    
        if flowers == 0:
            return True
        else:
            return False
                
        