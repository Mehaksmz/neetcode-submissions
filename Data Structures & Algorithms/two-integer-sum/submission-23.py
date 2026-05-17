class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numHash:
                return [numHash[complement], i]

            numHash[num] = i