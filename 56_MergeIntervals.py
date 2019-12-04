from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from functools import cmp_to_key

        def cmp(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                if a[1] < b[1]:
                    return -1
                elif a[1] > b[1]:
                    return 1
                else:
                    return 0
        intervals.sort(key=cmp_to_key(cmp))
        res = []
        temp = []
        for item in intervals:
            if not temp:
                temp.append(item)
            else:
                if temp[-1][1] >= item[0]:
                    if temp[-1][1] < item[1]:
                        temp.append(item)
                else:
                    res.append([temp[0][0], temp[-1][1]])
                    temp = [item]
        if temp:
            res.append([temp[0][0], temp[-1][1]])
        return res
