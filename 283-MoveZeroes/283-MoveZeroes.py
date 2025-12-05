# Last updated: 12/5/2025, 5:32:15 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        back = length - 1
        while back >= 0 and nums[back] == 0:
            back -= 1
        back += 1

        front = 0
        while front < back:
            if nums[front] == 0:
                nums[front:back - 1] = nums[front + 1: back]
                nums[back - 1] = 0
                back -= 1
            else:
                front += 1