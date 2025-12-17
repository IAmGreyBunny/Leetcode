# Last updated: 12/17/2025, 10:16:51 AM
1class Solution: 
2    def tribonacci(self, n: int) -> int:
3        ans = [0,1,1]
4        while n > len(ans)-1:
5            new_ans = ans[len(ans)-3] + ans[len(ans)-2] + ans[len(ans)-1] 
6            ans.append(new_ans)
7            print(ans)
8        
9        return ans[n]
10
11        