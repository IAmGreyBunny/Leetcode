# Last updated: 11/30/2025, 5:39:52 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowel_order = []
        vowel_index = []

        for i in range(0,len(s)):
            if s[i] in vowels:
                vowel_order.append(s[i])
                vowel_index.append(i)

        i=0
        j=len(vowel_order)-1
        while(i<j):
            temp = vowel_order[i]
            vowel_order[i] = vowel_order[j]
            vowel_order[j] = temp
            i+=1
            j-=1

        s = list(s)
        i=0
        for index in vowel_index:
            s[index] = vowel_order[i]
            i+=1
        
        s = "".join(s)
        return s
