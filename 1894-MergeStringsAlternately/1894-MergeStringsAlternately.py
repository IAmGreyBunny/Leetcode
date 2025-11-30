# Last updated: 11/30/2025, 5:39:42 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0

        result = ""

        while (i<len(word1) or j<len(word2)):
            
            # Search for alphanum in word1
            while i<len(word1):
                if word1[i].isalnum():
                    result+=word1[i]
                    i+=1
                    break
                else:
                    i+=1

            # Search for alphanum in word2
            while j<len(word2):
                if word2[j].isalnum():
                    result+=word2[j]
                    j+=1
                    break
                else:
                    j+=1

        return result

            