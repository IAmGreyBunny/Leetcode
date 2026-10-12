# Last updated: 10/12/2026, 4:45:41 PM
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest_altitude = current_altitude = 0

        for i in range(0,len(gain)):
            current_altitude+=gain[i]
            if current_altitude>highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude