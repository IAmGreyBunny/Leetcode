# Last updated: 12/17/2025, 10:17:12 AM
1class Solution: 
2    def tribonacci(self, n: int) -> int:
3        ans = [0,1,1]
4        while n > len(ans)-1:
5            ans.append(ans[len(ans)-3] + ans[len(ans)-2] + ans[len(ans)-1])
6        
7        return ans[n]
8
9        