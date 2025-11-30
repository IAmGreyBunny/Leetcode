# Last updated: 11/30/2025, 5:39:47 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = 0

        for i in range(0,len(gain)):
            current_altitude += gain[i]
            if current_altitude >= highest_altitude:
                highest_altitude = current_altitude
        
        return highest_altitude
            
        