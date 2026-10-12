# Last updated: 10/12/2026, 4:45:39 PM
class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in reversed(range(len(num))):
            if num[i] == "0":
                num = num[0:i]+num[i+1:]
            else:
                break
        return num