# Last updated: 10/12/2026, 4:45:52 PM
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = list(nums1-nums2)
        ans2 = list(nums2-nums1)
        
        return [ans1,ans2]