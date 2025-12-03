# Last updated: 12/3/2025, 7:42:05 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = ['a','e','i','o','u','A','E','I','O','U']
4        i = 0
5        j = len(s)-1
6
7        if len(s) <= 1:
8            return s
9
10        s = list(s)
11
12        while(i<j):
13            if s[i] in vowels:
14                if s[j] in vowels:
15                    s[i],s[j] = s[j],s[i]
16                    i+=1
17                    j-=1
18                else:
19                    j-=1
20            else:
21                i+=1
22        
23        s = ''.join(s)
24        return s