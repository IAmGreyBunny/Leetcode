# Last updated: 10/12/2026, 4:46:00 PM
class Solution: 
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c

        i=2        
        while i<n:
            a,b,c = b,c,a+b+c
            i+=1
        
        return c
        