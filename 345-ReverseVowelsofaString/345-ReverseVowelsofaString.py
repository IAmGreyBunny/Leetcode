# Last updated: 10/6/2026, 11:49:50 PM
1class Solution:
2    def reverseVowels(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        vowels = "AEIOUaeiou"
8        s = list(s)
9
10        i=0
11        j=len(s)-1
12
13        while i<len(s) and i<j:
14            if s[i] in vowels:
15                while j>i:
16                    if s[j] in vowels:
17                        s[i], s[j] = s[j], s[i]
18                        j-=1
19                        break
20                    j-=1
21            i+=1
22
23        return "".join(s)