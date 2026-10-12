# Last updated: 10/12/2026, 4:45:59 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            pass
        else:
            return ""
        
        result = ""

        i=0
        while(i<len(str1) and i<len(str2)):
            if str1[i] == str2[i]:
                result+=str1[i]
                i+=1
            else:
                break

        return result[:math.gcd(len(str1),len(str2))]
