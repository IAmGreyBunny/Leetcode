# Last updated: 11/30/2025, 5:57:42 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: str
7        """
8        result = ""
9        
10        for i in range(0,min(len(word1),len(word2))):
11
12            if word1 is not "":
13                result += word1[0]
14                word1 = word1[1:]
15            if word2 is not "":
16                result += word2[0]
17                word2 = word2[1:]
18        if len(word1) > 0:
19            result += word1
20        elif len(word2) >0:
21            result += word2
22        
23        return result
24        