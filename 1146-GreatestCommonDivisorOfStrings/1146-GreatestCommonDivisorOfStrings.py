# Last updated: 11/30/2025, 5:39:48 PM
import math

class Solution:
    

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ""

        if str1+str2 == str2+str1:
            pass
        else:
            return ""

        i=0
        j=0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                divisor += str1[i]
            else:
                break

            i+=1
            j+=1
    

        return divisor[0:math.gcd(len(str1), len(str2))]


        

    
        