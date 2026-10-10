# Last updated: 10/10/2026, 5:01:34 PM
1class Solution:
2    def largestAltitude(self, gain: list[int]) -> int:
3        highest_altitude = current_altitude = 0
4
5        for i in range(0,len(gain)):
6            current_altitude+=gain[i]
7            if current_altitude>highest_altitude:
8                highest_altitude = current_altitude
9
10        return highest_altitude