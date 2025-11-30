# Last updated: 11/30/2025, 5:39:51 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        start_search = 0

        i = 0

        for j in range(0,len(t)):
            
            if i == len(s):
                break

            if t[j] == s[i]:
                print(f"Comparing {s[i]} with {t[j]}")
                i+=1
        
        if i == len(s):
            return True
        else:
            return False