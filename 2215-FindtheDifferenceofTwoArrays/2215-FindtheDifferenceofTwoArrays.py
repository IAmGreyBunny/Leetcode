# Last updated: 12/12/2025, 3:17:26 PM
1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        # Declaring output 
4        nums1set, nums2set = set(nums1),set(nums2)
5        
6        return [list(nums1set-nums2set),list(nums2set-nums1set)]
7
8        
9