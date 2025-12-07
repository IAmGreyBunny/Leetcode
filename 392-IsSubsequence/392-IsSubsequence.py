# Last updated: 12/7/2025, 3:57:43 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3
4        start_search = 0
5
6        i = 0
7
8        for j in range(0,len(t)):
9            
10            if i == len(s):
11                break
12
13            if t[j] == s[i]:
14                print(f"Comparing {s[i]} with {t[j]}")
15                i+=1
16        
17        if i == len(s):
18            return True
19        else:
20            return False