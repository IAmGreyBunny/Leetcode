# Last updated: 12/1/2025, 4:04:13 PM
1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3
4        divisor = ""
5        
6        if str1+str2 == str2+str1:
7            pass
8        else:
9            return ""
10        
11        i=0
12        while(i<len(str1) and i<len(str2)):
13            if str1[i] == str2[i]:
14                divisor += str1[i]
15            else:
16                break
17            i+=1
18
19        return divisor[:math.gcd(len(str1),len(str2))]