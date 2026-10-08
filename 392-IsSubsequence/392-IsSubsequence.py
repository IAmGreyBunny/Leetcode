# Last updated: 10/9/2026, 12:01:21 AM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i=0
4        j=0
5
6        if len(s) == 0:
7            return True
8        
9        if len(s)==1:
10            return True if s in t else False
11
12        if len(s)>len(t):
13            return False
14        elif len(s)==len(t) and s != t:
15            return False
16
17        for i in range(0,len(t)):
18            if t[i] == s[j]:
19                j+=1
20
21            if j == len(s):
22                return True
23            
24        return False