class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        lst = [item[0] - item[1] for item in zip(gas, cost)]
        left, lack, start = 0, 0, 0
        for i, x in enumerate(lst):
            left += x
            if left < 0:
                lack += left
                left = 0
                start = i + 1
        return -1 if left + lack < 0 else start
