# Last updated: 10/12/2026, 4:45:55 PM
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}

        for num in arr:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1

        if len(count.values()) != len(set(count.values())):
            return False
        else:
            return True