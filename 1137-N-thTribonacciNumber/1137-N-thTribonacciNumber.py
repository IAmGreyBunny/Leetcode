# Last updated: 12/17/2025, 10:25:05 AM
1class Solution: 
2    def tribonacci(self, n: int) -> int:
3        a,b,c = 0,1,1
4        if n == 0:
5            return a
6        if n == 1:
7            return b
8        if n == 2:
9            return c
10
11        i=2        
12        while i<n:
13            a,b,c = b,c,a+b+c
14            i+=1
15        
16        return c
17        