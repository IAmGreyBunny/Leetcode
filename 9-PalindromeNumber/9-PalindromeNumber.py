# Last updated: 11/30/2025, 5:40:00 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        i = 0
        j = len(x)-1
        while(not (i>j)):
            if x[i] != x[j]:
                return False
            i+=1
            j-=1
        return True
        