class Solution:
    def maxArea(self, height):
        start, end = 0, len(height) - 1
        maximum = 0
        while start < end:
            left, right = height[start], height[end]
            maximum = max(maximum, (end - start) * min(left, right))
            if left < right:
                while start < end:
                    if height[start] > left:
                        break
                    start += 1
            else:
                while start < end:
                    if height[end] > right:
                        break
                    end -= 1

        return maximum
