from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)

        radius = 0
        i = 0
        for h in houses:
            while i < len(heaters) and heaters[i] < h:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - h)
            elif i == len(heaters):
                radius = max(radius, h - heaters[-1])
            else:
                radius = max(radius, min(heaters[i] - h, h - heaters[i - 1]))
        return radius
