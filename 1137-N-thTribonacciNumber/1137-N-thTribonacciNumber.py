# Last updated: 12/17/2025, 10:21:25 AM
1class Solution: 
2    def tribonacci(self, n: int) -> int:
3        ans = [0,1,1]
4        ans_len = len(ans)
5        while n > ans_len-1:
6            ans.append(ans[ans_len-3] + ans[ans_len-2] + ans[ans_len-1])
7            ans_len+=1
8        
9        return ans[n]
10
11        