# Last updated: 12/7/2025, 4:10:33 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        
4        #edge case
5        if len(s)==0:
6            return True
7        elif len(s) > len(t):
8            return False
9        elif len(t)==0:
10            if len(s) == 0:
11                return True
12            else:
13                return False
14
15        j=0
16        for i in range(0,len(t)):
17            if s[j] == t[i]:
18                j+=1
19            
20            # Matched entire subseq
21            if j == len(s):
22                return True
23
24        
25
26        return False
27