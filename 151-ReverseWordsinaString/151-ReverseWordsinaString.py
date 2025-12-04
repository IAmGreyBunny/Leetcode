# Last updated: 12/4/2025, 2:49:06 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        
4        words = []
5
6        # Edge cases
7        if len(s) <=1:
8            return s
9        
10        # Extract words
11        i=0
12        j=0
13
14        while i<=len(s):
15            if i<len(s) and s[i] is not " ":
16                i+=1
17            elif i==len(s):
18                if len(s[j:i]):
19                    words.append(s[j:i])
20                break
21            else:
22                if len(s[j:i])>0:
23                    words.append(s[j:i])
24                
25                # set j to the end of the word
26                j = i
27                # skip spaces
28                while j<len(s) and s[j] is " ":
29                    j+=1
30                i = j
31        words.reverse()
32        return " ".join(words)
33
34
35            