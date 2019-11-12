class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        for x1, y1 in points:
            d = dict()
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                dx = x1 - x2
                dy = y1 - y2
                diff = dx * dx + dy * dy

                if diff in d:
                    res += d[diff]
                    d[diff] += 1
                else:
                    d[diff] = 1
        return res * 2
