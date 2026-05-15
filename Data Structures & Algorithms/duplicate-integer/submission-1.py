class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])

        if len(num_set) == len(nums):
            return False
        else:
            return True

