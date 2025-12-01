# Last updated: 12/1/2025, 4:02:40 PM
1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3        import math
4
5        divisor = ""
6        
7        if str1+str2 == str2+str1:
8            pass
9        else:
10            return ""
11        
12        i=0
13        j=0
14        while(i<len(str1) and j<len(str2)):
15            if str1[i] == str2[j]:
16                divisor += str1[i]
17            else:
18                break
19            i+=1
20            j+=1
21
22        return divisor[:math.gcd(len(str1),len(str2))]