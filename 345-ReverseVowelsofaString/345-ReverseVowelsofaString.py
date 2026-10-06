# Last updated: 10/6/2026, 11:49:00 PM
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
17                        temp = s[i]
18                        s[i] = s[j]
19                        s[j] = temp
20                        j-=1
21                        break
22                    j-=1
23            i+=1
24
25        return "".join(s)