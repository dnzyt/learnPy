class Solution(object):
    def search(self, nums, target):

        def helper(start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[end]:
                if target > nums[mid]:
                    return helper(mid + 1, end)
                else:
                    return helper(start, mid - 1)
            else:
                if target > nums[mid]:
                    if nums[mid] > nums[end]:
                        return helper(mid + 1, end)
                    else:
                        if target <= nums[end]:
                            return helper(mid + 1, end)
                        else:
                            return helper(0, mid - 1)
                else:
                    if nums[mid] < nums[0]:
                        return helper(0, mid - 1)
                    else:
                        if target >= nums[0]:
                            return helper(0, mid - 1)
                        else:
                            return helper(mid + 1, end)

        return helper(0, len(nums) - 1)
