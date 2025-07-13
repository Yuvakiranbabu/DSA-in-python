class Solution:
    def twoSum(self, nums , target: int):

        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort based on numbers
        indexed_nums.sort()

        left = 0
        right = len(indexed_nums) - 1

        while left < right:
            subsum = indexed_nums[left][0] + indexed_nums[right][0]
            if subsum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif subsum > target:
                right -= 1
            else:
                left += 1

        return []  # if no solution found