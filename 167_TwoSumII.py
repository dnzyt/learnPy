class Solution:
    def twoSum(self, numbers, target):
        start, end = 0, len(numbers) - 1
        sum = 0
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                return [start + 1, end + 1]
