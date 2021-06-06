class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)

        n = len(nums)
        diff = 0
        result = 0

        for i in range(1, n):
            if nums[i-1] != nums[i]:
                diff += 1

            result += diff

        return result
